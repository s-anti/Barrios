<script>
	import Table from "../components/Table.svelte";
	import { _ } from "svelte-i18n";
	export let params = {};
	import AgregarLoteProp from "../lib/modals/agregar/AgregarLoteProp.svelte";
	let agregandoLote = false;
	import { tablasInfo } from "../store";
	import EditarPropietario from "../lib/modals/editar/EditarPropietario.svelte";
	let editando = false;

	const fetchData = (async () => {
		const response = await fetch(
			`http://127.0.0.1:5000/propietarios/${params.id}`
		);
		const data = await response.json();
		return data;
	})();

	fetchData.then((data) => {
		tablasInfo.update((valores) => {
			return {
				...valores,
				["propietarioInfo"]: data,
			};
		});
	});

	let dataProp = $tablasInfo["propietarioInfo"];
	$: dataProp = $tablasInfo["propietarioInfo"];
</script>

{#if $tablasInfo["propietarioInfo"] != null}
	<div class="flex w-full h-min items-center justify-evenly gap-5 p-12">
		<div class=" flex flex-col gap-5 bg-stone-700 rounded-xl p-5 h-full">
			<h1 class="text-3xl text-center capitalize">
				{$_("info")}
			</h1>
			{#each dataProp[0] as data, i}
				<div class=" bg-stone-500 w-full rounded-md">
					<p
						class="px-2 p-1 uppercase w-full border-b text-stone-200 border-stone-200 text-sm font-semibold"
					>
						{[$_("id"), $_("nombre"), $_("apellido")][i]}
					</p>
					<p class="px-2 p-1">{data}</p>
				</div>
			{/each}
			<div class="flex items-center gap-5 justify-evenly h-full">
				<div class="flex items-center justify-center">
					<button
						on:click={() => (editando = true)}
						class="hover:scale-110 shadow-md hover:shadow-xl transition rounded-full flex items-center justify-center"
					>
						<span
							class="rounded-full bg-stone-400 w-12 text-center flex items-center justify-center h-12 text-[2.3rem] material-icons-round"
							>edit</span
						>
					</button>
				</div>
				<div class="flex items-center justify-center">
					<button
						on:click={() => console.log("xd")}
						class="hover:scale-110 shadow-md hover:shadow-xl transition rounded-full flex items-center justify-center"
					>
						<span
							class="rounded-full bg-red-400 w-12 text-center flex items-center justify-center h-12 text-[2.3rem] material-icons-round"
							>close</span
						>
					</button>
				</div>
			</div>
		</div>
		<div class="  items-center flex w-min h-min gap-5 flex-col">
			<div
				class="xl:w-[68rem] 2xl:w-full lg:w-[50rem] sm:w-[32rem] md:w-[35rem]"
			>
				<Table
					rowNumber={3}
					columns={[
						[$_("id"), "texto"],
						[$_("lote"), "texto"],
						[$_("superficie"), "m2"],
						[$_("habitantes"), "texto"],
						[$_("vehiculos"), "texto"],
						[$_("luz"), "kw"],
						[$_("agua"), "m3"],
						[$_("gas"), "m3"],
						[$_("mes"), "texto"],
					]}
					table={"propietarios/" + params.id + "/consumos"}
					name=""
					altName="lotesConsumos"
					usaAgregar={true}
					funcAgregar={() => {
						agregandoLote = true;
					}}
					storeName="propietarioConsumos"
				/>
			</div>
			<div
				class="xl:w-[68rem] 2xl:w-full lg:w-[50rem] sm:w-[32rem] md:w-[35rem]"
			>
				<Table
					rowNumber={3}
					columns={[
						[$_("id"), "numero"],
						[$_("lote"), "lote"],
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
					table={"propietarios/" + params.id + "/pagos"}
					name=""
					altName="aPagar"
					usaEditar={true}
					funcEditar={() => {
						console.log("HACELO");
					}}
					storeName="propietarioPagos"
				/>
			</div>
		</div>
	</div>
{/if}
{#if agregandoLote && $tablasInfo["propietarioInfo"] != null}
	<AgregarLoteProp
		id={params.id}
		nombre={$tablasInfo["propietarioInfo"][0][1] +
			" " +
			$tablasInfo["propietarioInfo"][0][2]}
		funcCerrar={() => (agregandoLote = false)}
	/>
{/if}
{#if editando}
	<EditarPropietario
		cerrar={() => {
			editando = false;
		}}
		idEditando={params.id}
	/>
{/if}
