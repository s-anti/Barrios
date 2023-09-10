<script>
	import Table from "../components/Table.svelte";
	import { _ } from "svelte-i18n";
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
		funcAgregar={() => console.log("usaAgregar")}
		usaEditar={true}
		name="lotes"
		storeName="lotes"
		table="lotes"
	/>
</div>
