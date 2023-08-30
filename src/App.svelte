<script>
	import { _ } from "svelte-i18n";
	import Router from "svelte-spa-router";

	import Header from "./lib/Header.svelte";

	// const routes = {
	// 	"/": VistaDefault,
	// 	"/lotes": VistaLotes,
	// 	"/propietarios": VistaPropietarios,
	// 	"/consumos": VistaConsumos,
	// 	"/costos": VistaCostos,
	// 	"/propietarios/:id": VistaUnPropietario,
	// 	"*": Vista404,
	// };
</script>

<main class="h-full flex flex-col">
	<Header />

	<div class="flex flex-col max-w-full h-full bg-slate-700">
		<div class="flex max-w-full flex-col items-center h-full w-full">
			<!-- <Router {routes} /> -->
		</div>
		<div
			class="bg-slate-800 border-t border-green-400 shadow-inner rounded-t-lg"
		>
			<p class="p-2 text-center font-extralight text-slate-300">
				Santiago Piñero Cortez - 2023
			</p>
		</div>
	</div>
</main>
