<script>
	import Modal from "./Modal.svelte";
	import { tablasInfo } from "../../store";
	export let titulo;
	export let funcCerrar;
	export let tabla;
	let form;

	const enviar = async () => {
		const formData = new FormData(form);
		console.log("fechiando a ", `http://127.0.0.1:5000/cargar/${tabla}`);
		fetch(`http://127.0.0.1:5000/cargar/${tabla}`, {
			method: "POST",

			body: formData,
		});

		const response = await fetch(`http://127.0.0.1:5000/${tabla}`);
		const data = response.json();
		data.then((d) => {
			tablasInfo.update((valores) => {
				console.log("???");
				return {
					...valores,
					[tabla]: d,
				};
			});

			funcCerrar();
		});
	};
	import { _ } from "svelte-i18n";
</script>

<Modal {funcCerrar} {titulo}>
	<div
		slot="content"
		class="w-full flex flex-col items-center justify-evenly"
	>
		<form
			class="flex flex-col items-center h-full p-2"
			on:submit|preventDefault={enviar}
			id="form"
			bind:this={form}
		>
			<slot name="formContent" />
		</form>
		<button
			on:click={enviar}
			class="whitespace-nowrap flex items-center justify-center gap-2 bg-green-300 text-black p-2 rounded-lg transition hover:scale-110"
			><span class="uppercase font-semibold text-sm"
				>{$_("confirmar")}</span
			>
			<span class="flex items-center material-icons-round">check</span>
		</button>
	</div>
</Modal>
