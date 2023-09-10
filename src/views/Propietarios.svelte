<script>
	import Table from "../components/Table.svelte";
	import { _ } from "svelte-i18n";
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
		funcAgregar={() => console.log("usaAgregar")}
		usaExpandir={true}
		name="propietarios"
		table="propietarios"
		storeName="propietarios"
	/>
</div>
