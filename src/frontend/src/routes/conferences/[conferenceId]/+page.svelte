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
	<div class="options-container">
		<div>
			<h4>Author</h4>
			<a href="/conferences/{conferenceId}/submission">Submit an abstract</a>
		</div>
		{#if data.isReviewer}
			<div>
				<h4>Reviewer</h4>
				<a href="/conferences/{conferenceId}/review">Review</a>
			</div>
		{/if}
	</div>
</div>

<style>
	.options-container {
		display: flex;
		flex-direction: column;
		gap: 20px;
	}
</style>
