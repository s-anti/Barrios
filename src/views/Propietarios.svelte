<script>
	import Table from "../components/Table.svelte";
	import { _ } from "svelte-i18n";
	import AgregarPropietarios from "../lib/modals/agregar/AgregarPropietarios.svelte";

	let agregando = false;
</script>

<div class="flex items-center justify-center h-full p-10 m-10 max-w-full">
	<Table
		columns={[
			[$_("id"), "numero"],
			[$_("nombre"), "texto"],
			[$_("apellido"), "texto"],
			[$_("lotes"), "texto"],
		]}
		usaAgregar={true}
		funcAgregar={() => (agregando = true)}
		usaExpandir={true}
		name="propietarios"
		table="propietarios"
		storeName="propietarios"
	/>
	{#if agregando}
		<AgregarPropietarios funcCerrar={() => (agregando = false)} />{/if}
</div>
