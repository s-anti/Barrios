<script>
	export let name;
	export let usaAgregar;
	export let usaEditar;
	export let usaEliminar;
	export let columns;

	import { _ } from "svelte-i18n";
	import { tablasInfo } from "../store";

	let indexFrom = 0;
	let indexTo = 6;

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
	<div class="bg-secondary rounded-xl h-min-content p-5 w-full">
		<div class="flex items-center justify-between">
			<h1 class="pl-5 pb-2">{$_("viendo")} {$_(name)}</h1>
		</div>
		{#if $tablasInfo[name] !== null}
			<table
				class="min-w-full scrollbar overflow-x-auto border-separate border-spacing-y-3"
				on:wheel|preventDefault={scroll}
			>
				<thead>
					<tr class=" border-accent border-b">
						{#each columns as col}
							<th>{col[0]}</th>
						{/each}
						{#if usaEditar}
							<th>{$_("editar")}</th>
						{/if}
						{#if usaEliminar}
							<th>{$_("eliminar")}</th>
						{/if}
					</tr>
				</thead>
				<tbody class="">
					{#each $tablasInfo[name] as row}
						<tr class=" rounded-full">
							{#each row as data}
								<td
									class="text-center px-4 p-1 align-middle border-t border-opacity-0 border-x"
									>{data}</td
								>
							{/each}

							{#if usaEditar}
								<td
									class="border-t border-x border-opacity-0 p-1"
								>
									<button
										class="w-full h-full flex items-center justify-center"
									>
										<span
											class="rounded-full bg-background p-1 material-icons-round"
											>edit</span
										>
									</button>
								</td>
							{/if}
							{#if usaEliminar}
								<td
									class="border-t border-x border-opacity-0 p-1"
								>
									<button
										class="w-full h-full flex items-center justify-center"
									>
										<span
											class="rounded-full bg-background p-1 material-icons-round"
											>close</span
										>
									</button>
								</td>
							{/if}
						</tr>
					{/each}
				</tbody>
			</table>
		{/if}
	</div>
	{#if $tablasInfo[name] !== null}
		<div
			class="flex items-center gap-4 p-1 bg-primary rounded-md shadow-md w-fit justify-evenly"
		>
			{#each [...Array(Math.ceil($tablasInfo[name].length / 6)).keys()] as p}
				<button
					class=" flex items-center w-[24px]"
					on:click={() => {
						indexFrom = p * 6;
						indexTo = p * 6 + 6;
						console.log(indexFrom, indexTo);
					}}
				>
					<span class="text-center w-full">{p + 1}</span>
				</button>
			{/each}
		</div>
	{/if}
</div>
