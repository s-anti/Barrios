<script>
	export let name;

	export let usaAgregar = null;
	export let funcAgregar = null;

	export let usaEditar = null;
	export let funcEditar = null;

	export let usaEliminar = null;
	export let funcEliminar = null;

	export let usaExpandir = null;
	export let funcExpandir = null;

	export let columns;

	import { _ } from "svelte-i18n";
	import { tablasInfo } from "../store";

	export const rowNumber = 8;

	let indexFrom = 0;
	let indexTo = rowNumber;

	let pageHighlight = 0;

	const fetchData = (async () => {
		const response = await fetch(`http://127.0.0.1:5000/${name}`);
		const data = await response.json();
		return data;
	})();

	fetchData.then((data) => {
		tablasInfo.update((valores) => {
			return {
				...valores,
				[name]: data,
			};
		});
	});

	function scroll(e) {
		e.currentTarget.scrollLeft += e.deltaY * 0.3;
	}
</script>

<div
	class="w-full h-full p-10 flex items-center justify-between flex-col gap-5"
>
	<div class="bg-stone-700 shadow-sm rounded-xl h-min-content p-5 w-full">
		<div class="flex items-center justify-between pr-6">
			<p
				class="px-5 text-2xl flex items-center justify-center py-1 bg-stone-600 rounded-full"
			>
				{$_("viendo") + " " + $_(name)}
			</p>
			<p />
			{#if usaAgregar}
				<button
					on:click={funcAgregar}
					class="flex bg-emerald-400 text-black text-xl items-center justify-center gap-2 rounded-full"
				>
					<p class="p-2">{$_("agregar")}</p>
					<div
						class="material-icons-round pl-4 flex items-center justify-center after:shadow-2xl after:bg-emerald-300 after:content-['add'] after:p-4 after:rounded-full after:z-0 after:absolute"
					/>
				</button>
			{/if}
		</div>
		{#if $tablasInfo[name] !== null}
			<div class="relative mt-4 rounded-lg shadow-lg overflow-x-auto">
				<table
					class="min-w-full text-left bg-stone-600"
					on:wheel|preventDefault={scroll}
				>
					<thead class="uppercase bg-stone-500 text-sm">
						<tr class="">
							{#each columns as col}
								<th class="px-6 py-3" scope="col">{col[0]}</th>
							{/each}
							{#if usaEditar}
								<th
									class="border-l border-stone-400 text-center"
									scope="col">{$_("editar")}</th
								>
							{/if}
							{#if usaEliminar}
								<th
									class="border-l border-stone-400 text-center"
									scope="col">{$_("eliminar")}</th
								>
							{/if}
							{#if usaExpandir}
								<th
									class="border-l border-stone-400 text-center"
									scope="col">{$_("expandir")}</th
								>
							{/if}
						</tr>
					</thead>
					<tbody class="">
						{#each $tablasInfo[name].slice(indexFrom, indexTo) as row}
							<tr
								class="hover:bg-stone-500 hover:border-y transition hover:shadow-md border-t border-stone-500 p-2 rounded-full"
							>
								{#each row as data}
									<td
										class=" px-6 py-3 align-middle text-left"
										>{data}</td
									>
								{/each}

								{#if usaEditar}
									<td class="border-l border-stone-500 p-1">
										<div
											class="flex items-center justify-center"
										>
											<button
												on:click={funcEditar}
												class=" rounded-full flex items-center justify-center"
											>
												<span
													class="rounded-full bg-stone-400 p-1 material-icons-round"
													>edit</span
												>
											</button>
										</div>
									</td>
								{/if}
								{#if usaEliminar}
									<td class="border-l border-stone-500 p-1">
										<div
											class="flex items-center justify-center"
										>
											<button
												on:click={funcEliminar}
												class=" rounded-full flex items-center justify-center"
											>
												<span
													class="rounded-full bg-stone-400 p-1 material-icons-round"
													>close</span
												>
											</button>
										</div>
									</td>
								{/if}
								{#if usaExpandir}
									<td class="border-l border-stone-500 p-1">
										<div
											class="flex items-center justify-center"
										>
											<button
												on:click={funcExpandir}
												class=" rounded-full flex items-center justify-center"
											>
												<span
													class="rounded-full bg-stone-400 p-1 material-icons-round"
													>link</span
												>
											</button>
										</div>
									</td>
								{/if}
							</tr>
						{/each}
					</tbody>
				</table>
			</div>
		{/if}
	</div>
	{#if $tablasInfo[name] !== null}
		<div
			class="flex items-center gap-4 p-1 bg-primary rounded-lg bg-emerald-800 text-white shadow-md w-fit justify-evenly"
		>
			{#each [...Array(Math.ceil($tablasInfo[name].length / rowNumber)).keys()] as p}
				<button
					class=" flex rounded-full w-8 h-8 items-center {pageHighlight ===
					p
						? 'bg-emerald-300 text-black shadow-2xl '
						: 'bg-emerald-600 text-white   shadow-lg'} "
					on:click={() => (pageHighlight = p)}
					on:click={() => {
						indexFrom = p * rowNumber;
						indexTo = p * rowNumber + rowNumber;
						console.log(indexFrom, indexTo);
					}}
				>
					<span class="text-center w-full">{p + 1}</span>
				</button>
			{/each}
		</div>
	{/if}
</div>
