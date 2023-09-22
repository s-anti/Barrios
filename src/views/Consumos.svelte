<script>
	import Table from "../components/Table.svelte";
	import { _ } from "svelte-i18n";
	import { tablasInfo } from "../store";

	import EditarConsumos from "../lib/modals/editar/EditarConsumos.svelte";
	let editando = false;
	let idEditando = 0;

	const fetchData = async () => {
		const response = await fetch(`http://127.0.0.1:5000/consumos`);
		const data = await response.json();
		tablasInfo.update((valores) => {
			return {
				...valores,
				["consumos"]: data,
			};
		});
	};
</script>

<div class="">
	<button
		on:click={fetchData}
		class="m-4 text-black bg-red-100 p-2 rounded-full shadow-lg hover:bg-red-200 transition hover:scale-110 material-icons-round flex items-center justify-center"
		>refresh</button
	>
</div>

<div class="flex flex-col justify-center h-full px-10 mx-10 w-full">
	<Table
		columns={[
			[$_("id"), "numero"],
			[$_("lote"), "lote"],
			[$_("propietario"), "propietario"],
			[$_("mes"), "mes"],
			[$_("seguridad"), "plata"],
			[$_("consEle"), "plata"],
			[$_("consAgua"), "plata"],
			[$_("consGas"), "plata"],
			[$_("consLuzPublica"), "plata"],
			[$_("consAguaF"), "plata"],
			[$_("consAsfF"), "plata"],
			[$_("consGarage"), "plata"],
			[$_("total"), "total"],
			[$_("pagado"), "bool"],
		]}
		usaEditar={true}
		funcEditar={(id) => {
			idEditando = id;
			editando = true;
		}}
		name="consumos"
		table="consumos"
		storeName="consumos"
		rowNumber={7}
	/>
</div>

{#if editando}
	<EditarConsumos id={idEditando} cerrar={() => (editando = false)} />
{/if}
