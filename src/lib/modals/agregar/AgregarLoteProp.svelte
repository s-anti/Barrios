<script>
	import ModalAgregar from "../ModalAgregar.svelte";
	export let funcCerrar;
	export let id;
	export let nombre;
	import { _ } from "svelte-i18n";
	const fetchData = (async () => {
		const response = await fetch(`http://127.0.0.1:5000/lotes_de/${id}`);
		const data = await response.json();
		console.log("recibimo,s", data);

		return data;
	})();
</script>

<ModalAgregar {funcCerrar} tabla="proploteMes" titulo={$_("agregarLote")}>
	<div slot="formContent" class="flex gap-5 items-center justify-evenly">
		<div class="flex flex-col py-4 opacity-70">
			<label class="capitalize" for="pl_prop_id"
				>{$_("propietario")}</label
			>
			<input
				class="px-2 rounded-md text-white"
				type="text"
				required
				name="pl_prop_id"
				value={id}
				readonly
				id=""
			/>
			<p>{nombre}</p>
		</div>
		<div class="flex flex-col">
			<div class="flex flex-col py-4">
				<label class="capitalize" for="pl_lote_id">{$_("lote")}</label>
				{#await fetchData}
					cargando
				{:then data}
					<select
						class=" rounded-md outline-none px-2"
						name="pl_lote_id"
						required
						size="1"
					>
						{#each data as lote}
							<option value={lote}>{lote}</option>
						{/each}
					</select>
				{/await}
			</div>

			<div class="flex flex-col py-4 text-white">
				<label class="capitalize" for="pl_cons_mes">{$_("mes")}:</label>
				<input
					name="pl_cons_mes"
					class="rounded-md"
					type="month"
					required
				/>
			</div>

			<div class="flex flex-col py-4">
				<label class="capitalize" for="pl_superficie_cub"
					>{$_("supCubierta")}</label
				>
				<input
					name="pl_superficie_cub"
					class="rounded-md text-white"
					required
					type="number"
				/>
			</div>

			<div class="flex flex-col py-4">
				<label class="capitalize" for="pl_habitantes">
					{$_("habitantes")}
				</label>
				<input
					name="pl_habitantes"
					class="rounded-md text-white"
					required
					type="number"
				/>
			</div>
		</div>

		<div class="flex flex-col">
			<div class="flex flex-col py-4">
				<label class="capitalize" for="pl_vehiculos">
					{$_("vehiculos")}
				</label>
				<input
					name="pl_vehiculos"
					class="rounded-md text-white"
					required
					type="number"
				/>
			</div>

			<div class="flex flex-col py-4">
				<label class="capitalize" for="pl_cons_luz">
					{$_("consLuz")}
				</label>
				<input
					name="pl_cons_luz"
					class="rounded-md text-white"
					required
					type="number"
				/>
			</div>

			<div class="flex flex-col py-4">
				<label class="capitalize" for="pl_cons_agua">
					{$_("consAgua")}
				</label>
				<input
					name="pl_cons_agua"
					class="rounded-md text-white"
					required
					type="number"
				/>
			</div>

			<div class="flex flex-col py-4">
				<label class="capitalize" for="pl_cons_gas">
					{$_("consGas")}
				</label>
				<input
					name="pl_cons_gas"
					class="rounded-md text-white"
					required
					type="number"
				/>
			</div>
		</div>
	</div>
</ModalAgregar>
