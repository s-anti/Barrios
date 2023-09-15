<script>
	import Table from "../components/Table.svelte";
	import { _ } from "svelte-i18n";
	import AgregarLotes from "../lib/modals/agregar/AgregarLotes.svelte";
	let agregando = false;
</script>

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
		name="lotes"
		storeName="lotes"
		table="lotes"
	/>
	{#if agregando}
		<AgregarLotes funcCerrar={() => (agregando = false)} />
	{/if}
</div>
