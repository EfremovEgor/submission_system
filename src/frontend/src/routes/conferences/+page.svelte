<script>
	export let data;
	let conferences = data.conferences;
</script>

<svelte:head>
	<title>Events</title>
	<meta name="description" content="Home" />
</svelte:head>

<div class="container">
	<h3>Events</h3>
	{#if conferences.length}
		<table class="striped conferences-wrapper">
			<tbody>
				{#each conferences as conference}
					<tr class="conference-container">
						<td
							><a class="conference_page-button" href="/conferences/{conference.id}"
								>{conference.name}</a
							></td
						>
						<td
							><a class="submit-button" href="/conferences/{conference.id}/submission"
								>Submit an abstract</a
							></td
						>
						<td href=""
							><a class="learn_more-button" target="_blank" href={conference.site_url}>Learn More</a
							></td
						>
					</tr>
				{/each}
			</tbody>
		</table>
	{:else}
		<p aria-busy="true">Please wait while we are searching for available conferences</p>
	{/if}
</div>

<style>
	.submit-button,
	.learn_more-button,
	.conference_page-button {
	}
	.submit-button {
	}
	.learn_more-button {
	}
	.conference_page-button {
	}
	.conference-container {
	}
</style>
