<script lang="ts">
	import type { Clasificacion, IArticulo } from "$lib/interfaces/IArticulo";
	import "$lib/components/PageHeader.svelte";
	import PageHeader from "$lib/components/PageHeader.svelte";
	import RadioGroup from "$lib/components/SlideRadioGroup.svelte";
	import Articulo from "$lib/components/Articulo.svelte";
	import { Segmento } from "$lib/models/Segmento";
	import { Familia } from "$lib/models/Familia";
	import { Clase } from "$lib/models/Clase";
	import { Producto } from "$lib/models/Producto";
	import { agruparFaltantes, cargarExcel, getTestArticles } from "$lib/temp";
	const filters = ["Encontrados", "Dudosos", "Desconocidos"];
	let currFilter = $state<string>("");
	async function cargarArticulos(e: Event) {
		articulos = [];
		const datos = await cargarExcel(e);
		datos.forEach((row) => {
			if (!row?.id || !row?.nombre) return;
			const { id, nombre, descripcion, segmento, familia, clase, producto } =
				row;
			const clasificacion: Clasificacion = {
				articulo: {
					id,
					nombre,
					descripcion,
				},
				segmento: {},
				familia: {},
				clase: {},
				producto: {},
			};
			if (segmento)
				clasificacion.segmento = {
					confianza: 1,
					eleccion: new Segmento(String(row.segmento), "segmento", []),
				};
			if (familia)
				clasificacion.familia = {
					confianza: 1,
					eleccion: new Familia(String(row.familia), "familia", []),
				};
			if (clase)
				clasificacion.clase = {
					confianza: 1,
					eleccion: new Clase(String(row.clase), "clase", []),
				};
			if (producto)
				clasificacion.producto = {
					confianza: 1,
					eleccion: new Producto(String(row.producto), "producto"),
				};
			articulos.push(clasificacion);
		});
	}
	let articulos = $state<Clasificacion[]>(getTestArticles());
	function deleteArticle(i: number) {
		if (i !== -1) articulos.splice(i, 1);
	}
	let grupos = $derived(agruparFaltantes(articulos));
	let grupoActual = $derived(
		currFilter === "Encontrados"
			? grupos.productos
			: currFilter === "Desconocidos"
				? grupos.vacios
				: [...grupos.clases, ...grupos.familias, ...grupos.segmentos],
	);
	$effect(() => {});
</script>

<PageHeader title="CODIGOS DE SUNAT" />
<section class="selector"></section>
<section class="main">
	<section class="filtros">
		<div class="left">
			<label class="borded file">
				<input
					type="file"
					accept=".xlsx,.xls,.ods"
					onchange={cargarArticulos}
				/>
				Leer Excel
			</label>
			<button class="borded">Descargar Resultados</button>
		</div>
		<RadioGroup
			options={filters}
			title="mostrar articulos"
			bind:value={currFilter}
		/>
	</section>
	<section>
		<div class="resumen">
			<div>vacios: {grupos.vacios.length}</div>
			<div>hasta segmentos: {grupos.segmentos.length}</div>
			<div>hasta familias: {grupos.familias.length}</div>
			<div>hasta clases: {grupos.clases.length}</div>
			<div>clasificados: {grupos.productos.length}</div>
		</div>
	</section>
	<section class="table">
		{#each grupoActual as clasificacion, i}
			<Articulo {clasificacion} onDelete={() => deleteArticle(i)} />
		{/each}
	</section>
	<section></section>
</section>

<style>
	.resumen {
		display: flex;
		flex-wrap: wrap;
		gap: var(--size-l);
	}
	.main {
		display: flex;
		flex-direction: column;
		gap: var(--size-m);
		padding: var(--size-m);
	}
	.filtros {
		border: 2px 2px black solid;
		display: flex;
		flex-wrap: wrap;
		justify-content: space-between;
	}
	.filtros > .left {
		display: flex;
		gap: var(--size-s);
	}
	.filtros > .right {
		display: flex;
	}
	.table {
		display: flex;
		flex-direction: column;
		gap: var(--size-l);
	}
	.file {
		display: flex;
		align-items: center;
		padding: var(--size-m);
		input {
			width: 0;
			height: 0;
			overflow: hidden;
		}
	}
</style>
