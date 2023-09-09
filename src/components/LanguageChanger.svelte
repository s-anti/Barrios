<script>
	let currentLang = "🇺🇸";

	import { locale, locales } from "svelte-i18n";
	$locale = "en";

	console.log(locale, locales, $locale);

	let switchLang = () => {
		if ($locale == "es") {
			currentLang = "🇺🇸";
			$locale = "en";
		} else {
			currentLang = "🇦🇷";
			$locale = "es";
		}
	};
</script>

<div>
	<button
		class=" text-text p-0 h-fit flex bg-stone-300 items-center gap-2 border-2 border-black text-black px-2 rounded-full"
		on:click={switchLang}
	>
		<p class="material-icons-round text-2xl p-0">language</p>
		<p class="text-2xl p-0">{currentLang}</p>
	</button>
</div>
