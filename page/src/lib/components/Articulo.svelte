<script lang="ts">
	import type {
		Clasificacion,
		IArticulo,
		Seleccion,
	} from "$lib/interfaces/IArticulo";
	import { floatToPercentage } from "$lib/utils/numberUtils";
	interface Props {
		clasificacion: Clasificacion;
	}
	const { clasificacion: cls }: Props = $props();
	let seleccion = $state<null | Seleccion<any>>(null);
	let motivoActual = $state("");
	let editable = $state(false);

	$effect(() => {
		motivoActual = seleccion?.motivo ?? "";
	});
	let textoMotivo = $derived(
		seleccion
			? `(confianza ${floatToPercentage(seleccion?.confianza ?? 0)})`
			: "",
	);
</script>

<article class="articulo">
	<div class="left">
		<div class="nombre">
			<label class="borded">
				{editable ? "save" : "edit"}<input type="checkbox" name="editable" bind:checked={editable}>
			</label>
			{cls?.articulo.nombre}
		</div>
		<div class="descripcion">{cls?.articulo.descripcion}</div>
		<label class="motivo">
			<span>motivo de eleccion {textoMotivo}:</span>
			<textarea name="motivo" value={motivoActual} disabled={!editable}></textarea>
		</label>
	</div>
	<div class="right">
		<label class="borded">
			<input
				type="radio"
				name="clasificacion"
				value={cls?.segmento}
				bind:group={seleccion}
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
		<label class="borded">
			<input
				type="radio"
				name="clasificacion"
				value={cls?.clase}
				bind:group={seleccion}
			/>
			Clase: {cls?.clase?.eleccion?.nombre}
		</label>
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
</article>

<style>
	.articulo {
		padding: var(--size-s);
		border-radius: var(--size-m);
		border: var(--border-l);
		border-color: var(--border-color-auto);
		display: flex;
		gap: var(--size-m);
		& > * {
			flex: 1;
		}
	}
	.nombre {
		display: flex;
		font-size: var(--font-size-l);
		align-items: center;
		gap: var(--size-s);
		label{
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
		label {
			color: inherit;
			background-clip: border-box;
			position: relative;
			&:has(> input:checked) {
				
			}
		}
	}
	.left {
		display: flex;
		flex-direction: column;
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
