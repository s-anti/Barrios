<script>
	import { _ } from "svelte-i18n";
	let p;
</script>

<div class="flex w-full h-full items-center justify-center">
	<div
		class=" bg-red-500 p-5 gap-10 flex rounded-lg shadow-2xl h-min items-center justify-center"
	>
		<p
			class="animate-spin material-icons-round text-center text-3xl rounded-full w-10 h-10 flex items-center justify-center"
		>
			sentiment_dissatisfied
		</p>
		<h1 class=" text-center flex text-3xl uppercase">{$_("error")}</h1>
		<p class="text-center">{$_("errorTexto")}</p>
	</div>
</div>
