<script>
	import { onMount } from 'svelte';
	import api from '../../axios';
	let conferences = [];
	onMount(async () => {
		try {
			const response = await api.get('/conferences');
			conferences = response.data;
		} catch (error) {
			console.log(error);
		}
	});
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Home" />
</svelte:head>
<div class="container">
	{#if conferences.length}
		<ul>
			{#each conferences as conference}
				<li>
					<a class="secondary" href="/conferences/{conference.id}">{conference.name}</a>
				</li>
			{/each}
		</ul>
	{:else}
		<p aria-busy="true">Please wait while we are searching for available conferences</p>
	{/if}
</div>

<style>
</style>
