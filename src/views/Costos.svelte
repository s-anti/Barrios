<script>
	import Table from "../components/Table.svelte";
	import { _ } from "svelte-i18n";
</script>

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
	funcAgregar={() => console.log("usaAgregar")}
	usaEditar={true}
	usaEliminar={true}
	name="costos"
/>
