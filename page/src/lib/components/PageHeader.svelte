<script lang="ts">
    interface Props{
        title:string;
    }
    let {title}:Props = $props();
</script>

<section class="page-header">
    <h1>{title}</h1>
</section>

<style>
    .page-header{
        padding: var(--size-m);
    }
</style>