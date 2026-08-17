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
	import { agruparFaltantes, cargarExcel } from "$lib/temp";
	async function cargarArticulos(e: Event) {
		articulos = [];
		const datos = await cargarExcel(e);
		console.log(datos);
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
	let articulos = $state<Clasificacion[]>([
		{
			articulo: {
				id: "adwa",
				nombre: "Pollo a la brasa",
				descripcion: "nose que poner aa aaaa",
			},
			segmento: {
				motivo: "porque esta muy bonito",
				confianza: 0.9,
				eleccion: new Segmento("500000", "segmento", []),
			},
			familia: {
				eleccion: new Familia("", "familia"),
			},
			clase: {
				eleccion: new Clase("", "clase"),
			},
			producto: {
				eleccion: new Producto("", "producto"),
			},
		},
		{
			articulo: {
				id: "adwa2",
				nombre: "Pollo a la brasa",
				descripcion: "nose que poner aa aaaa",
			},
			segmento: {
				motivo: "porque esta muy bonito",
				confianza: 0.9,
				eleccion: new Segmento("500000", "segmento", []),
			},
			familia: {},
			clase: {},
			producto: {},
		},
	]);
	function deleteArticle(i: number) {
		if (i !== -1) articulos.splice(i, 1);
	}
	let faltantes = $derived(agruparFaltantes(articulos));
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
			options={["Encontrados", "Dudosos", "Desconocido"]}
			title="mostrar articulos"
		/>
	</section>
	<section>
		<div class="resumen">
			<div>vacios: {faltantes.vacios.length}</div>
			<div>hasta segmentos: {faltantes.segmentos.length}</div>
			<div>hasta familias: {faltantes.familias.length}</div>
			<div>hasta clases: {faltantes.clases.length}</div>
			<div>clasificados: {faltantes.productos.length}</div>
		</div>
	</section>
	<section class="table">
		{#each articulos as clasificacion, i}
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
