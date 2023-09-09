<script>
	import { _ } from "svelte-i18n";

	import Router from "svelte-spa-router";

	import Header from "./lib/Header.svelte";

	import Default from "./views/Default.svelte";
	import Vista404 from "./views/Vista404.svelte";
	import Propietarios from "./views/Propietarios.svelte";
	import Lotes from "./views/Lotes.svelte";
	import Consumos from "./views/Consumos.svelte";
	import Costos from "./views/Costos.svelte";

	// import VistaLotes from "./lib/routes/VistaLotes.svelte";
	// import VistaDefault from "./lib/routes/VistaDefault.svelte";
	// import Vista404 from "./lib/routes/Vista404.svelte";
	// import VistaPropietarios from "./lib/routes/VistaPropietarios.svelte";
	// @ts-ignore
	// import VistaConsumos from "./lib/routes/VistaConsumos.svelte";
	// import VistaCostos from "./lib/routes/VistaCostos.svelte";
	// import VistaUnPropietario from "./lib/routes/VistaUnPropietario.svelte";
	const routes = {
		"/": Default,
		"/propietarios": Propietarios,
		"/lotes": Lotes,
		"/consumos": Consumos,
		"/costos": Costos,
		// "/propietarios/:id": VistaUnPropietario,
		"*": Vista404,
	};
	import Table from "./components/Table.svelte";
</script>

<div class="h-full flex flex-col text-white bg-stone-800">
	<Header />
	<main class="flex flex-col max-w-full h-full">
		<div class="flex max-w-full flex-col items-center h-full w-full">
			<Router {routes} />
		</div>

		<div
			class="border-t-2 border-emerald-800 bg-stone-900 shadow-inner rounded-t-lg"
		>
			<p class="p-1 text-center font-extralight tracking-widest">
				Santiago Piñero Cortez - 2023
			</p>
		</div>
	</main>
</div>
