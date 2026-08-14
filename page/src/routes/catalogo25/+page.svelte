<script lang="ts">
	import type { Clasificacion, IArticulo } from "$lib/interfaces/IArticulo";
	import "$lib/components/PageHeader.svelte";
	import PageHeader from "$lib/components/PageHeader.svelte";
	import RadioGroup from "$lib/components/RadioGroup.svelte";
	import Articulo from "$lib/components/Articulo.svelte";
	const articulos: Clasificacion[] = [
		{
			articulo: {
				id: "adwa",
				nombre: "Pollo a la brasa",
				descripcion: "nose que poner aa aaaa",
			},
			segmento: {
				motivo: "porque esta muy bonito",
				confianza: 0.9,
				eleccion: { codigo: "500000", nombre: "segmento", familias: [] },
			},
			familia: {},
			clase: {},
			producto: {},
		},
	];
</script>

<PageHeader title="CODIGOS DE SUNAT" />
<section class="selector"></section>
<section class="tabla">
	<section class="filtros">
		<div class="left">
			<button>Importar Excel</button>
			<button>Descargar Resultados</button>
		</div>
		<RadioGroup
			options={["Encontrados", "Dudosos", "Desconocido"]}
			title="mostrar articulos"
		/>
	</section>
	<section class="table">
		{#each articulos as clasificacion, i}
			<Articulo {clasificacion} />
		{/each}
	</section>
</section>

<style>
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
	}
</style>
