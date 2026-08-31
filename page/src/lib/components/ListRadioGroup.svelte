<script lang="ts">
	import type { withClass } from "./componentTypes";
	import RadioInput from "./RadioInput.svelte";

	let {
		name,
		value,
		group = $bindable(),
		labels = [],
		class: className = "",
		options = [],
	}: withClass & {
		value?: string;
		name: string;
		group: any;
		labels: string[];
		options: Array<any>;
	} = $props();
</script>

<div class={className}>
	{#each options as option, i}
		<RadioInput {group} value={option} name="clasificacion" class="radiobutton">
			{labels?.[i]}
		</RadioInput>
	{/each}
</div>
