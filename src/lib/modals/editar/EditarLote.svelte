<script>
	import ModalEditar from "../ModalEditar.svelte";
	import { tablasInfo } from "../../../store";
	export let cerrar;
	export let idEditando;
	import { _ } from "svelte-i18n";

	const fetchData = (async () => {
		const response = await fetch(
			`http://127.0.0.1:5000/uno_solo/lotes/${idEditando}`
		);
		const data = await response.json();
		return data;
	})();

	if ($tablasInfo == null) {
		console.log("Es null y salió todo mal");
	}
</script>

<ModalEditar {cerrar} tabla="lotes" titulo={$_("editandoLote")}>
	<div slot="formContent">
		{#await fetchData}
			<p class="capitalize">{$_("cargando")}</p>
			<!-- Spinner -->
		{:then data}
			<div class="flex gap-20 p-2">
				<div class="flex flex-col justify-evenly items-center">
					<div
						class="flex w-full items-stretch justify-stretch gap-3"
					>
						<div class="w-full">
							<label class="capitalize" for="lote_id">ID:</label>
							<input
								class="text-white w-10 px-2 rounded-md"
								type="text"
								name="lote_id"
								id="lote_id"
								value={Object.values(data[0])}
								readonly
							/>
						</div>

						<div class="w-full">
							<label class="capitalize" for="lote_manz_id"
								>{$_("manzana")}</label
							>
							<input
								class="text-white w-10 px-2 rounded-md"
								type="text"
								name="lote_manz_id"
								id="lote_manz_id"
								value={Object.values(data[1])}
								readonly
							/>
						</div>
					</div>
					<div>
						<p class="capitalize">{$_("propietario")}</p>
						{#if Object.values(data[8])[0] != null}
							<p class="text-stone-300 capitalize font-light">
								{Object.values(data[8])}
							</p>
						{:else}
							<p class="text-stone-300 capitalize font-light">
								{$_("ninguno")}
							</p>
						{/if}
						<input
							class="rounded-md pl-2"
							type="select"
							required
							readonly
							value={Object.values(data[8])[0]}
						/>
						<!-- TODO: que le pase una lista de los nombres de los propietarios -->
					</div>
					<div>
						<p class="capitalize">{$_("metrosFrente")}</p>
						<p class="text-stone-300 capitalize font-light">
							{Object.values(data[2])}
						</p>
						<input
							class="rounded-md pl-2"
							size="6"
							type="number"
							accept=""
							name="lote_m_frente"
							value={Object.values(data[2])}
							required
							min="0"
						/>
					</div>
					<div>
						<p class="capitalize">{$_("metrosProf")}</p>
						<p class="text-stone-300 capitalize font-light">
							{Object.values(data[3])}
						</p>
						<input
							class="rounded-md pl-2"
							size="6"
							type="number"
							accept=""
							name="lote_m_prof"
							value={Object.values(data[3])}
							required
							min="0"
						/>
					</div>
				</div>
				<div class="flex flex-col justify-evenly items-stretch">
					<div>
						<p class="capitalize">{$_("tieneLuz")}</p>
						<div class="flex w-full justify-between">
							<p class="text-stone-300 capitalize font-light">
								{$_("antes")}:
							</p>
							{#if String(Object.values(data[4])) == "true"}
								<span
									class="material-icons-round font-black bg-stone-500 rounded-full text-green-500 w-7 h-7 flex items-center justify-center"
									>check</span
								>
							{:else}
								<span
									class="material-icons-round font-black bg-stone-500 rounded-full text-red-500 w-7 h-7 flex items-center justify-center"
									>close</span
								>
							{/if}
						</div>
						<div
							class="flex w-full items-center justify-between pb-2"
						>
							<div>
								<input
									type="radio"
									id="lote_luz_bool_false"
									name="lote_luz_bool"
									value={0}
								/>
								<label
									for="lote_luz_bool_false"
									class="capitalize">{$_("no")}</label
								>
							</div>
							<div>
								<input
									type="radio"
									id="lote_luz_bool_true"
									name="lote_luz_bool"
									value={1}
								/>
								<label
									for="lote_luz_bool_true"
									class="capitalize">{$_("si")}</label
								>
							</div>
						</div>
						<span class="border-b p-1 m-1 w-full block" />
					</div>

					<div>
						<p class="capitalize">{$_("tieneAgua")}</p>
						<div class="flex w-full justify-between">
							<p class="text-stone-300 capitalize font-light">
								{$_("antes")}:
							</p>
							{#if String(Object.values(data[5])) == "true"}
								<span
									class="material-icons-round font-black bg-stone-500 rounded-full text-green-500 w-7 h-7 flex items-center justify-center"
									>check</span
								>
							{:else}
								<span
									class="material-icons-round font-black bg-stone-500 rounded-full text-red-500 w-7 h-7 flex items-center justify-center"
									>close</span
								>
							{/if}
						</div>
						<div
							class="flex w-full items-center justify-between pb-2"
						>
							<div>
								<input
									type="radio"
									id="lote_agua_bool_false"
									name="lote_agua_bool"
									value={0}
								/>
								<label
									for="lote_agua_bool_false"
									class="capitalize">{$_("no")}</label
								>
							</div>
							<div>
								<input
									type="radio"
									id="lote_agua_bool_true"
									name="lote_agua_bool"
									value={1}
								/>
								<label
									for="lote_agua_bool_true"
									class="capitalize">{$_("si")}</label
								>
							</div>
						</div>
						<span class="border-b p-1 m-1 w-full block" />
					</div>

					<div>
						<p class="capitalize">{$_("tieneAsfalto")}</p>
						<div class="flex w-full justify-between">
							<p class="text-stone-300 capitalize font-light">
								{$_("antes")}:
							</p>
							{#if String(Object.values(data[6])) == "true"}
								<span
									class="material-icons-round font-black bg-stone-500 rounded-full text-green-500 w-7 h-7 flex items-center justify-center"
									>check</span
								>
							{:else}
								<span
									class="material-icons-round font-black bg-stone-500 rounded-full text-red-500 w-7 h-7 flex items-center justify-center"
									>close</span
								>
							{/if}
						</div>
						<div
							class="flex w-full items-center justify-between pb-2"
						>
							<div>
								<input
									type="radio"
									id="lote_asf_bool_false"
									name="lote_asf_bool"
									value={0}
								/>
								<label
									for="lote_asf_bool_false"
									class="capitalize">{$_("no")}</label
								>
							</div>
							<div>
								<input
									type="radio"
									id="lote_asf_bool_true"
									name="lote_asf_bool"
									value={1}
								/>
								<label
									for="lote_asf_bool_true"
									class="capitalize">{$_("si")}</label
								>
							</div>
						</div>
						<span class="border-b p-1 m-1 w-full block" />
					</div>

					<div>
						<p class="capitalize">{$_("tieneEsquina")}</p>
						<div class="flex w-full justify-between">
							<p class="text-stone-300 capitalize font-light">
								{$_("antes")}:
							</p>
							{#if String(Object.values(data[7])) == "true"}
								<span
									class="material-icons-round font-black bg-stone-500 rounded-full text-green-500 w-7 h-7 flex items-center justify-center"
									>check</span
								>
							{:else}
								<span
									class="material-icons-round font-black bg-stone-500 rounded-full text-red-500 w-7 h-7 flex items-center justify-center"
									>close</span
								>
							{/if}
						</div>
						<div
							class="flex w-full items-center justify-between pb-2"
						>
							<div>
								<input
									type="radio"
									id="lote_esq_bool_false"
									name="lote_esq_bool"
									value={0}
								/>
								<label
									for="lote_esq_bool_false"
									class="capitalize">{$_("no")}</label
								>
							</div>
							<div>
								<input
									type="radio"
									id="lote_esq_bool_true"
									name="lote_esq_bool"
									value={1}
								/>
								<label
									for="lote_esq_bool_true"
									class="capitalize">{$_("si")}</label
								>
							</div>
						</div>
						<span class="border-b p-1 m-1 w-full block" />
					</div>
				</div>

				<!-- Dueño -->

				<!-- {#each data as i}
					<div class="flex bg-purple-300 flex-col p-2">
						<p>
							{Object.values(i)}
						</p>
						<input
                        class="rounded-md pl-2" type="text" name={Object.keys(i)[0]} id="" />
					</div>
				{/each} -->
			</div>
		{/await}
	</div>
</ModalEditar>
