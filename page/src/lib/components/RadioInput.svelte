<script lang="ts">
	import type { Snippet } from "svelte";
	import type { withClass } from "./componentTypes";
	import type { Seleccion } from "$lib/interfaces/IArticulo";

	type Props = {
		group: any;
		name: string;
		value: any;
		children?: Snippet;
		onClear?: () => any;
	} & withClass;

	let {
		group = $bindable(),
		name,
		value = $bindable(),
		children,
		class: className = "",
		onClear,
	}: Props = $props();

	function keyDownHandler(e: KeyboardEvent) {
		if (e.key === "Delete") onClear?.();
	}
	const show = $derived(!!value.eleccion);
</script>

<label class={"borded " + className}>
	<input type="radio" {name} {value} bind:group onkeydown={keyDownHandler} />
	<div>{@render children?.()}</div>
	{#if show}
		<button tabindex="-1" onclick={onClear}>x</button>
	{/if}
</label>

<style>
	label {
		padding-inline: var(--size-s);
		display: flex;
		div {
			flex-grow: 1;
		}
		button {
			background: none;
			opacity: 0;
		}
		&:focus-within,
		&:has(:checked),
		&:hover {
			button {
				opacity: 1;
			}
		}
	}
</style>
