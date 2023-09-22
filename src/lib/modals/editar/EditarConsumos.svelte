<script>
	import ModalEditar from "../ModalEditar.svelte";
	import { tablasInfo } from "../../../store";
	import { _ } from "svelte-i18n";
	export let cerrar;
	export let id;

	let checked = false;
	let fecha = null;

	for (const r of $tablasInfo["consumos"]) {
		if (r[0] == id) {
			checked = r[13] ? true : false;
			fecha = r[13];
		}
	}
</script>

<ModalEditar {cerrar} tabla="consumos" titulo={$_("editandoConsumo")}>
	<div slot="formContent">
		<div class="w-full gap-3 flex flex-col transition">
			<div class="w-full">
				<label class="capitalize" for="cons_id">ID:</label>
				<input
					class="text-white w-10 px-2 rounded-md bg-stone-500"
					type="text"
					name="cons_id"
					id="cons_id"
					value={id}
					readonly
				/>
			</div>
			<label class="capitalize flex items-center gap-3">
				<span>
					{$_("pagado")}:
				</span>
				<input
					type="checkbox"
					class="form-checkbox h-6 w-6 text-red-600"
					bind:checked
				/>
			</label>

			{#if checked}
				<div class="flex items-center gap-3">
					<label class="capitalize" for="cons_fecha_pago"
						>{$_("fechaPago")}:</label
					>

					<input
						name="cons_fecha_pago"
						class="rounded-md"
						type="month"
						bind:value={fecha}
						required
					/>
				</div>
			{/if}
		</div>
	</div>
</ModalEditar>
