<script>
	export let data;
</script>

<div class="container">
	{#each data.user.reviewer_in as conference}
		<ul>
			<li><a href="reviewer/{conference.acronym}">{conference.name}</a></li>
		</ul>
	{/each}
</div>
