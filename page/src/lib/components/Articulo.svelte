<script lang="ts">
	import type {
		Clasificacion,
		IArticulo,
		Seleccion,
	} from "$lib/interfaces/IArticulo";
	import type { ISegmento } from "$lib/interfaces/ISegmento";
	import type { IFamilia } from "$lib/interfaces/IFamilia";
	import type { IClase } from "$lib/interfaces/IClase";
	import { floatToPercentage } from "$lib/utils/numberUtils";
	import RadioInput from "./RadioInput.svelte";
	import { Segmento } from "$lib/models/Segmento";
	import { Familia } from "$lib/models/Familia";
	import { Clase } from "$lib/models/Clase";
	interface Props {
		clasificacion: Clasificacion;
		onDelete?: () => any;
	}
	const { clasificacion: cls = $bindable(), onDelete }: Props = $props();
	let seleccion = $state<undefined | Seleccion<any>>(undefined);
	let descripcion = $state("");
	let motivoActual = $state("");
	let editable = $state(false);
	const name = $derived("clasificacion-" + cls.articulo.id);

	$effect(() => {
		descripcion = cls.articulo?.descripcion ?? "";
	});
	$effect(() => {
		motivoActual = seleccion?.motivo ?? "";
	});
	$effect(() => {
		if (editable) return;
		cls.articulo.descripcion = descripcion;
		if (seleccion) seleccion.motivo = motivoActual;
	});
	let textoMotivo = $derived(
		seleccion
			? `(confianza ${floatToPercentage(seleccion?.confianza ?? 0)})`
			: "",
	);
	function limpiarSeleccion(sl: Seleccion<any>) {
		if(!sl) return;
		const { eleccion } = sl;
		if (eleccion instanceof Segmento) limpiarSeleccion(cls.familia);
		else if(eleccion instanceof Familia) limpiarSeleccion(cls.clase);
		else if(eleccion instanceof Clase) limpiarSeleccion(cls.producto);
		sl.confianza = undefined;
		sl.motivo = undefined;
		sl.eleccion = undefined;
	}
</script>

<article class="articulo">
	<div class="left">
		<div class="header">
			<span class="nombre">{cls?.articulo.nombre}</span>
		</div>
		<label class="descripcion">
			<input
				disabled={!editable}
				type="text"
				name="motivo"
				bind:value={descripcion}
			/>
		</label>
		<label class="motivo">
			<span>motivo de eleccion {textoMotivo}:</span>
			<textarea
				tabindex="0"
				name="motivo"
				bind:value={motivoActual}
				disabled={!editable}
			></textarea>
		</label>
	</div>
	<div class="right">
		<RadioInput
			{name}
			value={cls?.segmento}
			bind:group={seleccion}
			class="radiobutton"
			onClear={() => {
				limpiarSeleccion(cls.segmento);
			}}
		>
			Segmento: {cls?.segmento?.eleccion?.nombre}
		</RadioInput>
		<RadioInput
			{name}
			value={cls?.familia}
			bind:group={seleccion}
			class="radiobutton"
			onClear={() => limpiarSeleccion(cls.familia)}
		>
			Familia: {cls?.familia?.eleccion?.nombre}
		</RadioInput>
		<RadioInput
			bind:group={seleccion}
			value={cls?.clase}
			{name}
			class="radiobutton"
			onClear={() => limpiarSeleccion(cls.clase)}
		>
			Clase: {cls.clase?.eleccion?.nombre}
		</RadioInput>
		<RadioInput
			bind:group={seleccion}
			value={cls?.producto}
			{name}
			class="radiobutton"
			onClear={() => limpiarSeleccion(cls.producto)}
		>
			Producto: {cls?.producto?.eleccion?.nombre}
		</RadioInput>
	</div>
	<div class="buttons">
		<label class="borded large">
			<button onclick={onDelete}>delete</button>
		</label>
		<label class="borded large">
			{editable ? "save" : "edit"}<input
				type="checkbox"
				name="editable"
				bind:checked={editable}
			/>
		</label>
	</div>
</article>

<style>
	.articulo {
		position: relative;
		padding: var(--size-s);
		--padding-bottom: var(--size-l);
		border-radius: var(--size-m);
		border-style: solid;
		border-width: var(--border-l);
		border-color: var(--border-color-auto);
		display: flex;
		gap: var(--size-m);
		& > * {
			flex: 1;
		}
		&:hover > .buttons {
			transition: opacity 0.16s;
			opacity: 1;
		}
	}
	.buttons {
		display: flex;
		gap: var(--size-s);
		box-sizing: border-box;
		width: 100%;
		transition: opacity 0.25s;
		opacity: 0;
		position: absolute;
		top: calc(100% + var(--size-s));
		padding-inline: calc(var(--size-s) * 2);
		left: 0;
		transform: translate(0, -50%);
		z-index: 1;
		&:has(input:checked),
		&:focus-within {
			transition: opacity 0.16s;
			opacity: 1;
		}
		label {
			background-color: white;
		}
	}
	.header {
		display: flex;
		font-size: var(--font-size-l);
		align-items: center;
		padding-inline: var(--size-s);
		gap: var(--size-s);
		.nombre {
			flex-grow: 1;
		}
		label {
			font-size: initial;
		}
	}
	.descripcion {
		font-size: var(--font-size-m);
		margin-bottom: var(--size-s);
	}
	.right {
		display: flex;
		flex-direction: column;
		gap: var(--size-xs);
		label:has(> input:not(:checked)) {
			outline-width: 0px;
		}
		:global(.radiobutton:has(> input:not(:checked))) {
			outline-width: 0px;
		}
	}
	.left {
		display: flex;
		flex-direction: column;
	}
	label.descripcion {
		background: none;
		input {
			width: 100%;
		}
	}
	label.motivo {
		border-radius: var(--size-s);
		padding: var(--size-xs) var(--size-s);
		background-color: oklch(from currentColor var(--l-5) c h);
		display: flex;
		flex-direction: column;
		flex-grow: 1;
		span {
			display: flex;
			width: 100%;
		}
		> textarea {
			flex-grow: 1;
		}
	}
</style>
