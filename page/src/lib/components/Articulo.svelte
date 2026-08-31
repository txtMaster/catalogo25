<script lang="ts">
	import {
		limpiarSeleccion,
		type Clasificacion,
		type Seleccion,
	} from "$lib/interfaces/IArticulo";
	import { floatToPercentage } from "$lib/utils/numberUtils";
	import RadioInput from "./RadioInput.svelte";
	import { Segmento } from "$lib/models/Segmento";
	import { Familia } from "$lib/models/Familia";
	import { Clase } from "$lib/models/Clase";
	import ListRadioGroup from "./ListRadioGroup.svelte";
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
	const labels = $derived([
		`Segmento: ${cls.segmento?.eleccion?.nombre ?? ""}`,
		`Familia: ${cls.familia?.eleccion?.nombre ?? ""}`,
		`Clase: ${cls.clase?.eleccion?.nombre ?? ""}`,
		`Producto: ${cls.producto?.eleccion?.nombre ?? ""}`,
	]);
	const options = $derived([
		cls?.segmento,
		cls?.familia,
		cls?.clase,
		cls?.producto,
	]);
	$effect((): any => (descripcion = cls.articulo?.descripcion ?? ""));
	$effect((): any => (motivoActual = seleccion?.motivo ?? ""));
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
	function limpiarJerarquia(sl: Seleccion<any>) {
		if (!sl) return;
		const { eleccion } = sl;
		if (eleccion instanceof Segmento) limpiarJerarquia(cls.familia);
		else if (eleccion instanceof Familia) limpiarJerarquia(cls.clase);
		else if (eleccion instanceof Clase) limpiarJerarquia(cls.producto);
		limpiarSeleccion(sl);
	}
</script>

<article class="articulo">
	<div class="left">
		<div class="header">
			<span class="nombre">{cls?.articulo.nombre +" - "+ cls.articulo.id}</span>
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
		{#each options as option, i}
			<RadioInput
				bind:group={seleccion}
				value={option}
				{name}
				class="radiobutton"
				onClear={() => limpiarJerarquia(option)}
			>
				{labels?.[i]}
			</RadioInput>
		{/each}
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
