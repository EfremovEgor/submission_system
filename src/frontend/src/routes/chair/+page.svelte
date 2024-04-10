<script>
	export let data;
</script>

<div class="container">
	{#each data.user.chair_in as conference}
		<ul>
			<li><a href="chair/{conference.acronym}">{conference.name}</a></li>
		</ul>
	{/each}
</div>
