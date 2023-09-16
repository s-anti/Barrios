<script>
	import Modal from "./Modal.svelte";
	import { tablasInfo } from "../../store";
	export let titulo;
	export let tabla;
	export let cerrar;
	import { _ } from "svelte-i18n";

	let form;

	const enviar = async () => {
		console.log("form es: ", form);

		const formData = new FormData(form);
		console.log("formData es: ", formData);

		for (var [key, value] of formData.entries()) {
			console.log("AAAAAAAA", key, value);
		}
		fetch(`http://127.0.0.1:5000/editar/${tabla}`, {
			method: "POST",

			body: formData,
		});

		const response = await fetch(`http://127.0.0.1:5000/${tabla}`);
		const data = response.json();
		data.then((d) => {
			tablasInfo.update((valores) => {
				return {
					...valores,
					[tabla]: d,
				};
			});
		});
		cerrar();
	};
	// ESTO LO COPIAMOS PERO PONELE QUE TRANQUI
	// LO PODRÍAMOS ELEVAR A Modal.SVELTE PERO FUE
</script>

<Modal {titulo} funcCerrar={cerrar}>
	<div slot="content">
		<form
			class="flex items-center flex-col gap-10 justify-evenly"
			on:submit|preventDefault={enviar}
			id="form"
			bind:this={form}
		>
			<slot name="formContent" />
			<button
				type="submit"
				class="whitespace-nowrap flex items-center justify-center gap-2 bg-green-300 text-black p-2 rounded-lg transition hover:scale-110"
				><span class="uppercase font-semibold text-sm"
					>{$_("confirmar")}</span
				>
				<span class="flex items-center material-icons-round">check</span
				>
			</button>
		</form>
	</div>
</Modal>
