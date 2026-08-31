<script lang="ts">
	import SlideRadioGroup from "./SlideRadioGroup.svelte";
	let {
		filters = [],
		views = [],
		indexFilter = $bindable(0),
		indexView = $bindable(0),
	}: {
		filters?: string[];
		views?: string[];
		indexView?: number;
		indexFilter?: number;
	} = $props();
</script>

<section class="filtro-articulos">
	{#if filters.length !== 0}
		<SlideRadioGroup
			class="slideradio"
			options={filters}
			name="tipo-articulos"
			title="mostrar articulos"
			bind:position={indexFilter}
		/>
	{/if}
	{#if views.length !== 0}
		<SlideRadioGroup
			class="slideradio"
			options={views}
			name="modo-vista"
			title="modo de vista"
			bind:position={indexView}
		/>
	{/if}
</section>

<style>
	.filtro-articulos {
		display: flex;
		width: 100%;
		justify-content: space-between;
		flex-wrap: wrap;
		gap: var(--size-s);
	}
	:global(html.mobile) .filtro-articulos {
		:global(.slideradio) {
			width: 100%;
			flex-grow: 1;
		}
	}
</style>
