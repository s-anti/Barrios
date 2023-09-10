import { writable } from "svelte/store";

export const mesTrabajando = writable("2023-08");

export const tablasInfo = writable({
	propietarios: null,
	lotes: null,
	consumos: null,
	costos: null,
	propietarioConsumos: null,
	propietarioLotes: null,
	propietarioInfo: null,
	propietarioPagos: null,
});

export const dataAhora = writable(null);

export let idioma = "en";
