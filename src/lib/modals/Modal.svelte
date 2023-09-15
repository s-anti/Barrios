<script>
	export let funcCerrar;
	export let titulo;
</script>

<!-- svelte-ignore a11y-no-static-element-interactions -->
<!-- svelte-ignore a11y-click-events-have-key-events -->
<div
	class="flex items-center justify-center absolute top-0 h-full w-full bg-stone-900 bg-opacity-70"
	on:click={funcCerrar}
>
	<div
		class=" rounded-lg bg-stone-600 shadow-xl opacity-100"
		on:click|stopPropagation
	>
		<div
			class="bg-stone-500 w-full p-5 rounded-lg flex items-center gap-5 justify-between"
		>
			<h1 class="capitalize text-lg font-semibold">{titulo}</h1>
			<button
				on:click={funcCerrar}
				class="bg-red-500 flex items-center justify-center rounded-full w-10 h-10 material-icons-round"
			>
				close
			</button>
		</div>
		<div class="p-5">
			<slot name="content" class="p-5" />
		</div>
	</div>
</div>
