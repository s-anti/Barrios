<script>
	import Table from "../components/Table.svelte";
	import { _ } from "svelte-i18n";
</script>

<div class="flex items-center justify-center h-full p-10 m-10 w-full">
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
		usaAgregar={true}
		funcAgregar={() => console.log("usaAgregar")}
		usaEditar={true}
		name="consumos"
		table="consumos"
		storeName="consumos"
	/>
</div>
