<script>
	import Table from "../components/Table.svelte";
	import { _ } from "svelte-i18n";
	import { mesTrabajando } from "../store";
	let mes = "2023-08";

	let xd = async () => {
		fetch(`http://127.0.0.1:5000/${$mesTrabajando}`);
	};
	$: {
		mesTrabajando.set(mes);
		xd();
	}
</script>

<div class="m-4 bg-stone-600 p-2 rounded-full shadow-lg">
	<label for="mesAhora" class="capitalize pr-2">{$_("mes")}:</label>
	<input
		bind:value={mes}
		class=" rounded-lg pl-1"
		name="mesAhora"
		type="month"
		on:change={xd}
	/>
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
		funcAgregar={() => console.log("usaAgregar")}
		usaEditar={true}
		name="consumos"
		table="consumos"
		storeName="consumos"
	/>
</div>
