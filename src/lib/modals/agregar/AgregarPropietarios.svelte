<script>
	import ModalAgregar from "../ModalAgregar.svelte";
	export let funcCerrar;
	import { _ } from "svelte-i18n";
</script>

<ModalAgregar titulo={$_("agregarProps")} {funcCerrar} tabla="propietarios">
	<div slot="formContent" class="h-full flex flex-col p-4">
		<div class="flex flex-col py-4">
			<label for="prop_nombre" class="capitalize">{$_("nombre")}:</label>
			<input
				class="bg-white text-black rounded-md outline-none px-2"
				type="text"
				name="prop_nombre"
				required
			/>
		</div>
		<div class="flex flex-col py-4">
			<label for="prop_apellido" class="capitalize"
				>{$_("apellido")}:</label
			>
			<input
				class="bg-white text-black rounded-md outline-none px-2"
				type="text"
				name="prop_apellido"
				required
			/>
		</div>
	</div>
</ModalAgregar>
