<script>
	import Table from "../components/Table.svelte";
	import { _ } from "svelte-i18n";
	import AgregarLotes from "../lib/modals/agregar/AgregarLotes.svelte";
	let agregando = false;
	import EditarLote from "../lib/modals/editar/EditarLote.svelte";
	let editando = false;
	let idEditando = null;
</script>

<!-- <EditarLote cerrar={() => console.log("xd")} idEditando="1" /> -->
<div class="flex items-center justify-center h-full p-10 m-10 w-full">
	<Table
		columns={[
			[$_("id"), "numero"],
			[$_("manzana"), "numero"],
			[$_("propietario"), "propietario"],

			[$_("metrosFrente"), "metros"],
			[$_("metrosProf"), "metros"],
			[$_("luz"), "bool"],
			[$_("gas"), "bool"],
			[$_("asf"), "bool"],
			[$_("esq"), "bool"],
		]}
		usaAgregar={true}
		funcAgregar={() => (agregando = true)}
		usaEditar={true}
		funcEditar={(id) => {
			idEditando = id;
			editando = true;
		}}
		name="lotes"
		storeName="lotes"
		table="lotes"
	/>
	{#if agregando}
		<AgregarLotes funcCerrar={() => (agregando = false)} />
	{/if}
	{#if editando && idEditando != null}
		<EditarLote cerrar={() => (editando = false)} {idEditando} />
	{/if}
</div>
