<script lang="ts">
	import type { Clasificacion } from "$lib/interfaces/IArticulo";
	import { generateDescription } from "$lib/temp";

	const {
		vacios = new Set(),
		segmentos = new Set(),
		familias = new Set(),
		clases = new Set(),
		sinDescripcion = new Set(),
		productos = new Set(),
	}: {
		vacios?: Set<Clasificacion>;
		segmentos?: Set<Clasificacion>;
		familias?: Set<Clasificacion>;
		clases?: Set<Clasificacion>;
		sinDescripcion?: Set<Clasificacion>;
		productos?: Set<Clasificacion>;
	} = $props();

	function onGenerarDescripcion() {
		generateDescription([...sinDescripcion]);
	}
</script>

<section class="articulo-resultados w-full">
	<h3>RESULTADOS</h3>
	<div class="options">
		<div class={sinDescripcion.size > 0 ? "show" : ""}>
			{sinDescripcion.size} articulos sin descripcion
			<button class="link" onclick={onGenerarDescripcion}>revisar</button>
		</div>
		<div class={vacios.size > 0 ? "show" : ""}>
			{vacios.size} articulos desconocidos
			<button class="link">generar</button>
		</div>
		<div class={segmentos.size > 0 ? "show" : ""}>
			{segmentos.size} articulos sin familias
			<button class="link">generar</button>
		</div>
		<div class={familias.size > 0 ? "show" : ""}>
			{familias.size} articulos sin clases
			<button class="link">generar</button>
		</div>
		<div class={clases.size > 0 ? "show" : ""}>
			{clases.size} articulos sin codigo final
			<button class="link">generar</button>
		</div>
	</div>
</section>

<style>
	.articulo-resultados {
		display: flex;
		flex-direction: column;
		gap: var(--size-s);
	}
	.options {
		display: grid;
		grid-template-rows: 1fr 1fr;
		grid-template-columns: repeat(auto-fit, minmax(min(20rem, 100%), 1fr));
		row-gap: var(--size-s);
		column-gap: var(--size-m);
		& > * {
			display: none;
			text-wrap: nowrap;
			align-items: stretch;
			gap: var(--size-s);
			&.show {
				display: flex;
			}
		}
	}
	:global(html.mobile) {
		.options {
			& > * {
				align-items: start;
				gap: var(--size-xs);

				button {
				}
			}
		}
	}
</style>
