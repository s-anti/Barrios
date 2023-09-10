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
	import UnPropietario from "./views/UnPropietario.svelte";

	const routes = {
		"/": Default,
		"/propietarios": Propietarios,
		"/lotes": Lotes,
		"/consumos": Consumos,
		"/costos": Costos,
		"/propietarios/:id": UnPropietario,
		"*": Vista404,
	};
</script>

<div class="h-full flex flex-col overflow-hidden text-white bg-stone-800">
	<Header />
	<main class="flex flex-col max-w-full h-full">
		<div class="flex max-w-full flex-col items-center h-full w-full">
			<Router {routes} />
		</div>

		<div
			class="border-t-2 border-emerald-800 bg-stone-900 shadow-inner rounded-t-lg flex items-center justify-center overflow-clip"
		>
			<a
				class="  w-min whitespace-nowrap text-xl text-center font-extralight p-1 px-2 rounded-full hover:scale-110 block transition hover:underline tracking-widest"
				href="https://github.com/s-anti"
			>
				Santiago Piñero Cortez - 2023
			</a>
		</div>
	</main>
</div>
