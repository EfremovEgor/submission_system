<script>
	import { page } from '$app/stores';
	export let data;
	const conferenceId = $page.params.conferenceId;
	let conferenceData = data.conference;
</script>

<svelte:head>
	<title>Conference</title>
	<meta name="description" content="Home" />
</svelte:head>
<div class="container">
	<h3>{conferenceData.name}</h3>
	<div>
		<a href="/conferences/{conferenceId}/submission">Submit</a>
	</div>
	{#if data.isReviewer}
		<div>
			<a href="/conferences/{conferenceId}/review">Review</a>
		</div>
	{/if}
</div>

<style>
</style>
