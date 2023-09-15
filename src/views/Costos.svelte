<script>
	import Table from "../components/Table.svelte";
	import { _ } from "svelte-i18n";
	import AgregarCosto from "../lib/modals/agregar/agregarCosto.svelte";
	let agregando = false;
</script>

<div class="flex items-center justify-center h-full p-10 m-10 w-full">
	<Table
		columns={[
			[$_("id"), "numero"],
			[$_("cos_seguridad"), "plata"],
			[$_("cos_kw"), "plata"],
			[$_("cos_m3_agua"), "plata"],
			[$_("cos_m3_gas"), "plata"],
			[$_("cos_total_luz"), "plata"],
			[$_("cos_mf_agua"), "plata"],
			[$_("cos_mf_asf"), "plata"],
			[$_("cos_vehiculo"), "plata"],
			[$_("cos_m2_terreno"), "plata"],
			[$_("cos_mes"), "mes"],
		]}
		usaAgregar={true}
		funcAgregar={() => {
			agregando = true;
		}}
		usaEditar={true}
		usaEliminar={true}
		name="costos"
		storeName="costos"
		table="costos"
	/>
	{#if agregando}
		<AgregarCosto
			funcCerrar={() => {
				agregando = false;
			}}
		/>
	{/if}
</div>
