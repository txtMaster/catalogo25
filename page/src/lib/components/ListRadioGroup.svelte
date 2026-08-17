<script lang="ts">
	import type { withClass } from "./componentTypes";

	let {
		name,
		value,
        group = $bindable(),
        class:className ="",
        options = []
	}: withClass & {
		value?: string;
		name: string;
        group:any;
        options:Array<any>;
	} = $props();
</script>

<div class={className}>
    {#each options as option,i}
        
    {/each}
	<label class="borded">
		<input
			type="radio"
			{name}
			{value}
			{group}
			checked
		/>
		Segmento: {cls?.segmento?.eleccion?.nombre}
	</label>
	<label class="borded">
		<input
			type="radio"
			name="clasificacion"
			value={cls?.familia}
			bind:group={seleccion}
		/>
		Familia: {cls?.familia?.eleccion?.nombre}
	</label>
	<RadioInput
		group={seleccion}
		value={cls?.producto}
		name="clasificacion"
		class="radiobutton"
	>
		Clase: {cls.clase?.eleccion?.nombre}
	</RadioInput>
	<label class="borded">
		<input
			type="radio"
			name="clasificacion"
			value={cls?.producto}
			bind:group={seleccion}
		/>
		Producto: {cls?.producto?.eleccion?.nombre}
	</label>
</div>
