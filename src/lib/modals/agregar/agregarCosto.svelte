<script>
	import ModalAgregar from "../ModalAgregar.svelte";
	export let funcCerrar;
	import { _ } from "svelte-i18n";
</script>

<ModalAgregar tabla="costos" titulo={$_("agregarPrecios")} {funcCerrar}>
	<div slot="formContent" class=" w-full h-full flex gap-20 p-4">
		<div>
			<div class="flex flex-col py-4">
				<label for="cos_seguridad">{$_("seguridadFijo")}</label>
				<input
					class="bg-white text-black rounded-md outline-none px-2"
					type="number"
					name="cos_seguridad"
					required
				/>
			</div>

			<div class="flex flex-col py-4">
				<label for="cos_kw">{$_("cosKw")}</label>
				<input
					class="bg-white text-black rounded-md outline-none px-2"
					type="number"
					name="cos_kw"
					required
				/>
			</div>

			<div class="flex flex-col py-4">
				<label for="cos_m3_agua">{$_("m3Agua")}</label>
				<input
					class="bg-white text-black rounded-md outline-none px-2"
					type="number"
					name="cos_m3_agua"
					required
				/>
			</div>
			<div class="flex flex-col py-4">
				<label for="cos_m3_gas">{$_("m3Gas")}</label>
				<input
					class="bg-white text-black rounded-md outline-none px-2"
					type="number"
					name="cos_m3_gas"
					required
				/>
			</div>

			<div class="flex flex-col py-4">
				<label for="cos_total_luz">{$_("cosTotLuz")}</label>
				<input
					class="bg-white text-black rounded-md outline-none px-2"
					type="number"
					name="cos_total_luz"
					required
				/>
			</div>
		</div>

		<div>
			<div class="flex flex-col py-4">
				<label for="cos_mf_agua">{$_("cosAguaFrente")}</label>
				<input
					class="bg-white text-black rounded-md outline-none px-2"
					type="number"
					name="cos_mf_agua"
					required
				/>
			</div>

			<div class="flex flex-col py-4">
				<label for="cos_mf_asf">{$_("cosAsfFrente")}</label>
				<input
					class="bg-white text-black rounded-md outline-none px-2"
					type="number"
					name="cos_mf_asf"
					required
				/>
			</div>

			<div class="flex flex-col py-4">
				<label for="cos_vehiculos">{$_("cochPorVehiculo")}</label>
				<input
					class="bg-white text-black rounded-md outline-none px-2"
					type="number"
					name="cos_vehiculos"
					required
				/>
			</div>

			<div class="flex flex-col py-4">
				<label for="cos_m2_valor">{$_("precioM2Terreno")}</label>
				<input
					class="bg-white text-black rounded-md outline-none px-2"
					type="number"
					name="cos_m2_valor"
					required
				/>
			</div>

			<div class="flex flex-col py-4">
				<label for="cos_mes">{$_("mesPrecios")}</label>
				<input
					class="text-white bg-stone-800 rounded-md outline-none px-2"
					type="month"
					name="cos_mes"
					required
				/>
			</div>
		</div>

		<!-- >TODO mes -->
	</div>
</ModalAgregar>
