<script>
	import Icon from '@iconify/svelte';
	import { page } from '$app/stores';
	import { convertToDate } from '../../../utils';

	export let data;
	const conferenceAcronym = $page.params.conferenceAcronym;
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
	</h3>
	<div class="actions-container">
		<a class="link" href="/conferences/{conferenceAcronym}/submission">Submit an abstract</a>
		<a class="link" href={conferenceData.site_url} target="_blank">Learn more</a>
	</div>
	<div class="options-container">
		<div class="time_details">
			<p>
				Submission Deadline: {conferenceData.submission_deadline != null
					? convertToDate(conferenceData.submission_deadline)
					: ''}
			</p>
			<p>
				Start Date: {conferenceData.start_date != null
					? convertToDate(conferenceData.start_date)
					: ''}
			</p>
		</div>
		<div class="description">
			{@html conferenceData.description}
		</div>
		{#each Object.keys(categories) as category}
			<b>{category}</b>
			<ul>
				{#each categories[category] as topic}
					<li>
						{topic.name}
					</li>
				{/each}
			</ul>
		{/each}
	</div>
</div>

<style>
	.actions-container {
		display: flex;
		gap: 50px;
		margin-bottom: 20px;
	}
	.blue-button {
		width: 250px;
	}

	.options-container {
		display: flex;
		flex-direction: column;
	}
</style>
