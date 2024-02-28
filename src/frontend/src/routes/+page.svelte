<script>
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	onMount(async () => {
		goto('/conferences');
	});
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Home" />
</svelte:head>
<div class="container">
	<h1>Main page</h1>
</div>

<style>
</style>
