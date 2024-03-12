<script>
	import Icon from '@iconify/svelte';
	import { page } from '$app/stores';
	export let data;
	const conferenceId = $page.params.conferenceId;
	let conferenceData = data.conference;
	let categories = {};
	conferenceData.topics.forEach((element) => {
		if (categories[element.category] == undefined) categories[element.category] = [element];
		else categories[element.category].push(element);
	});
</script>

<svelte:head>
	<title>Conference</title>
	<meta name="description" content="Home" />
</svelte:head>
<div class="container">
	<h3>
		{conferenceData.name}
		<a target="_blank" href={conferenceData.site_url}><Icon icon="material-symbols-light:link" /></a
		>
	</h3>
	<div class="options-container">
		<details>
			<summary>Description</summary>
			<p>{conferenceData.description}</p>
			<p><b>Symposiums:</b></p>
			{#each Object.keys(categories) as category}
				<p>{category}</p>
				<ul>
					{#each categories[category] as topic}
						<li>
							{topic.name}
						</li>
					{/each}
				</ul>
			{/each}
		</details>
		<div>
			<a class="blue-button" role="button" href="/conferences/{conferenceId}/submission"
				>Submit an abstract</a
			>
		</div>

		{#if data.isReviewer}
			<div>
				<a class="blue-button" role="button" href="/conferences/{conferenceId}/review">Review</a>
			</div>
		{/if}
	</div>
</div>

<style>
	summary {
		max-width: fit-content;
	}
	.blue-button {
		width: 250px;
	}
	.options-container {
		display: flex;
		flex-direction: column;
		gap: 20px;
	}
</style>
