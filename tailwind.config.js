import { text } from "svelte/internal";

/** @type {import('tailwindcss').Config} */
export default {
	content: ["./src/**/*.{html,js,svelte,ts}"],
	theme: {
		extend: {
			colors: {
				text: "#ebfcff",
				background: "#00090a",
				primary: "#90edfe",
				secondary: "#00272d",
				accent: "#02d3f7",
			},
		},
	},
	plugins: [],
};
