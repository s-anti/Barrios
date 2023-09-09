<script>
	import Table from "../components/Table.svelte";
	import { _ } from "svelte-i18n";
</script>

<Table
	columns={[
		[$_("id"), "numero"],
		[$_("nombre"), "texto"],
		[$_("apellido"), "texto"],
		[$_("lotes"), "texto"],
	]}
	usaAgregar={true}
	funcAgregar={() => console.log("usaAgregar")}
	usaExpandir={true}
	funcExpandir={() => console.log("usaExpandir")}
	name="propietarios"
/>
