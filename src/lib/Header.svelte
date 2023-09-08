<script>
	import { _ } from "svelte-i18n";
	import { link } from "svelte-spa-router";
	let highlightedIndex = 4;

	import LanguageChanger from "../components/LanguageChanger.svelte";
</script>

<div class="w-full flex justify-between p-2 items-center">
	<ul class="flex gap-4 flex-1">
		<a
			use:link
			href="/propietarios"
			class="capitalize p-2 items-center text-center rounded-lg {highlightedIndex ===
			0
				? 'bg-primary text-background'
				: 'bg-secondary'} "
			on:click={() => (highlightedIndex = 0)}
		>
			{$_("propietarios")}
		</a>

		<a
			use:link
			href="/lotes"
			class="capitalize p-2 items-center text-center rounded-lg {highlightedIndex ===
			1
				? 'bg-primary text-background'
				: 'bg-secondary'} "
			on:click={() => (highlightedIndex = 1)}
		>
			{$_("lotes")}
		</a>

		<a
			use:link
			href="/consumos"
			class="capitalize p-2 items-center text-center rounded-lg {highlightedIndex ===
			2
				? 'bg-primary text-background'
				: 'bg-secondary'} "
			on:click={() => (highlightedIndex = 2)}
		>
			{$_("consumos")}
		</a>

		<a
			use:link
			href="/costos"
			class="capitalize p-2 items-center text-center rounded-lg {highlightedIndex ===
			3
				? 'bg-primary text-background'
				: 'bg-secondary'} "
			on:click={() => (highlightedIndex = 3)}
		>
			{$_("costos")}
		</a>
	</ul>
	<div class="flex-1 flex items-center justify-center">
		<h1 class="text-3xl font-black tracking-wide">{$_("titulo")}</h1>
	</div>

	<div class="flex-1 gap-3 flex w-full justify-end">
		<LanguageChanger />
	</div>
</div>
