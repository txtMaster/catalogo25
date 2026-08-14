<script lang="ts">
	interface Props {
		options: Array<string>;
		title: string;
	}
	let { title, options }: Props = $props();
	let position = $state(0);
</script>

<div class="radio-group">
	<div class="title">{title}</div>
	<section class="options" style:--i={position} style:--list={options.length}>
		{#each options as option, i}
			<label>
				{option.trim()}<input
					type="radio"
					name="tipo"
					value={i}
					bind:group={position}
				/>
			</label>
		{/each}
	</section>
</div>

<style>
	.radio-group {
		--padding: var(--size-xs);
		--line-padding: calc(var(--padding) * 2);
		--list: 0;
		border-radius: var(--size-m);
		font-size: smaller;
		display: flex;
		flex-direction: column;
		.title {
			padding-inline: var(--line-padding);
		}
		.options {
			user-select: none;
			position: relative;
			--i: 0;
			--option-size: calc((100% / var(--list)) - (var(--padding)));
			font-size: var(--size-m);
			display: grid;
			grid-auto-flow: column;
			grid-auto-columns: 1fr;
			column-gap: var(--padding);
			padding: var(--padding);
			border-radius: inherit;
			border: var(--border-l);
			border-color: oklch(from currentColor var(--l-3) c h);
			isolation: isolate;
			label {
				padding: var(--padding) var(--line-padding);
				width: 100%;
				display: flex;
				border-radius: inherit;
				justify-content: center;
				box-sizing: border-box;
			}
			&::before {
				transition: left 0.2s;
				border-radius: inherit;
				top: 50%;
				transform: translateY(-50%);
				left: calc(
					var(--padding) +
						((var(--option-size) + (var(--padding) / 2)) * var(--i))
				);
				content: "";
				position: absolute;
				background: oklch(0.9 0 0);
				z-index: -1;
				height: calc(100% - var(--line-padding));
				width: var(--option-size);
			}
		&:has(input:focus-within) {
				border-color: oklch(from currentColor var(--l-2) c h);
			}
		}
		input {
			appearance: none;
			width: 0;
			height: 0;
		}
	}
</style>
