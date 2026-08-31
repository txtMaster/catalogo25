<script lang="ts">
	import type { Clasificacion } from "$lib/interfaces/IArticulo";
	import "$lib/components/PageHeader.svelte";
	import PageHeader from "$lib/components/PageHeader.svelte";
	import Articulo from "$lib/components/Articulo.svelte";
	import { SvelteSet } from "svelte/reactivity";
	import {
		agruparFaltantes,
		cargarArticulosDeExcel,
		getTestArticles,
	} from "$lib/temp";
	import FiltroArticulos from "$lib/components/FiltroArticulos.svelte";
	import ArticuloResultados from "$lib/components/ArticuloResultados.svelte";
	import ClasificacionButtonDownload from "$lib/components/ClasificacionButtonDownload.svelte";
	const filters = ["Encontrados", "Dudosos", "Desconocidos"];
	const views = ["Articulo", "Tabla", "Agrupado"];
	let indexFilter = $state<number>(0);
	let currFilter = $derived(filters?.[indexFilter]);
	let pais = $state("");
	let rubro = $state("");
	async function cargarArticulos(e?: Event) {
		articulos = {};
		ordenArticulos.clear()

		let newArticles = [];
		if (e) {
			newArticles = await cargarArticulosDeExcel(e);
		} else {
			newArticles = getTestArticles();
		}
		newArticles.forEach((cls) => {
			ordenArticulos.add(cls.articulo.id);
			articulos[cls.articulo.id] = cls;
		});
	}
	let ordenArticulos: Set<string> = new SvelteSet();
	let articulos = $state<{[key:string]:Clasificacion}>({});
	cargarArticulos();
	function deleteArticle(i: string) {
		if (!articulos[i]) return;
		delete articulos[i];
		ordenArticulos.delete(i);
	}

	let grupos = $derived(agruparFaltantes(articulos, ordenArticulos));
	let grupoDudosos = $derived(
		new SvelteSet([...grupos.clases, ...grupos.familias, ...grupos.segmentos]),
	);
	let grupoActual = $derived(
		currFilter === "Encontrados"
			? grupos.productos
			: currFilter === "Desconocidos"
				? grupos.vacios
				: grupoDudosos,
	);
</script>

<PageHeader title="CODIGOS DE SUNAT" />
<section class="selector">
	<div class="top flex between">
		<div class="contexto flex col grow">
			<h3>DATOS Y CONTEXTO</h3>
			<label
				>Pais:
				<input type="text" bind:value={pais} />
			</label>
			<label
				>Rubro:
				<input type="text" bind:value={rubro} />
			</label>
		</div>
		<div class="carga h-fit">
			<label class="file link">
				<input
					class="hide"
					type="file"
					accept=".xlsx,.xls,.ods"
					onchange={cargarArticulos}
				/>
				Leer Excel
			</label>
			<ClasificacionButtonDownload clasificaciones={articulos}/>
		</div>
	</div>
	<div class="resultados">
		<ArticuloResultados
			sinDescripcion={grupos.sinDescripcion}
			vacios={grupos.vacios}
			segmentos={grupos.segmentos}
			familias={grupos.familias}
			clases={grupos.clases}
		/>
	</div>
</section>
<section class="main">
	<section class="filtros">
		<FiltroArticulos bind:indexFilter {filters} {views} />
	</section>
	<section class="table">
		{#each grupoActual as clasificacion (clasificacion.articulo.id)}
			<Articulo
				{clasificacion}
				onDelete={() => deleteArticle(clasificacion.articulo.id)}
			/>
		{/each}
	</section>
	<section></section>
</section>

<style>
	.main {
		display: flex;
		flex-direction: column;
		gap: var(--size-m);
		padding: var(--size-m);
	}
	.filtros {
		position: sticky;
		top: var(--size-s);
		padding: var(--size-s);
		border-radius: var(--size-l);
		display: flex;
		flex-wrap: wrap;
		justify-content: space-between;
		z-index: 2;
		background-color: oklch(1 0 0 / 0.5);
		box-shadow:
			1px 2px 6px 2px oklch(0.7 0 0 / 0.3),
			0 0 6px 4px oklch(1 0 0 / 0.5) inset;
		backdrop-filter: blur(var(--size-s));
	}
	.table {
		display: flex;
		flex-direction: column;
		gap: var(--size-l);
		height: 90vh;
		overflow: hidden scroll;
	}
	.file {
		display: flex;
		align-items: center;
	}
	.selector {
		margin-inline: var(--size-m);
		padding: var(--size-m);
		border-radius: var(--size-m);
		border: solid;
		border-width: var(--border-l);
		border-color: var(--border-color-auto);
		display: flex;
		flex-direction: column;
		gap: var(--size-m);
		.top {
			display: flex;
			row-gap: var(--size-m);
		}
		.carga {
			display: flex;
			flex-wrap: wrap;
			gap: var(--size-s);
			& > * {
				flex-grow: 1;
			}
		}
	}

	:global(html.mobile) {
		.selector {
			.top {
				flex-direction: column-reverse;
			}
		}
	}
	.contexto{
		label{
			display: flex;
			gap: var(--size-s);
		}
	}
</style>
