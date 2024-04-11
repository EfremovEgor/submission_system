<script>
	export let data;
	import { review_statuses } from '../../../../utils';
	
	import Icon from '@iconify/svelte';
	let to_display = data.submissions;
	let categories = {};
	let checked_topics = {};
	function count_submissions(topic) {
		let counter = 0;
		data.submissions.forEach((element) => {
			if (element.topic.name == topic) counter++;
		});
		return counter;
	}
	data.submissions.forEach((element) => {
		let topic = element.topic;
		if (categories[topic.category] == null) categories[topic.category] = [];
		if (!categories[topic.category].includes(topic.name))
			categories[topic.category].push(topic.name);
	});

	function filterSubmissions() {
		to_display = [];
		data.submissions.forEach((element) => {

			if (checked_topics[element.topic.name]){
				to_display.push(element);}
		});
	}
	async function setStatus(id, status) {
		const response = await fetch('/api/submissions/setStatus', {
			method: 'POST',
			body: JSON.stringify({ id: id, review_result: status }),
			headers: {
				'content-type': 'application/json'
			}
		});
		const total = await response.json();
	}
	
	Object.values(categories).forEach((element) => {
		element.forEach(topic => {
			checked_topics[topic] = true;
		});
		
	});
</script>

<svelte:head>
	<title>Conference</title>
	<meta name="description" content="Home" />
</svelte:head>
<div class="container">
	<h3>{data.conference.name}</h3>
	<details open>
		<summary style="width: fit-content;">Choose Topic</summary>
		<table style="max-width: 700px;">
			{#each Object.keys(categories) as category}
				<tr><td colspan="3"><b>{category}</b></td></tr>

				{#each categories[category] as topic}
					<tr>
						<td
							><input
								bind:checked={checked_topics[topic]}
								on:change={filterSubmissions}
								type="checkbox"
								name={topic}
							/></td
						>
						<td>{topic}</td>
						<td>{count_submissions(topic)}</td>
					</tr>
				{/each}
			{/each}
		</table>
	</details>
	<span>Displayed: {to_display.length}/{data.submissions.length} <br /></span>
	<button style="padding:0" class="bare_button">Export to Excel</button>
	<table class="striped">
		<thead>
			<td>#</td>
			<td>Authors</td>
			<td>Title</td>
			<td>Topic</td>
			<td>Report Format</td>
			<td>Created At</td>
			<td>View</td>
			<td>Review status</td>
		</thead>
		{#each to_display as submission, i}
			<tr>
				<td>{submission.id}</td>
				<td
					>{#each submission.authors as author}
						<span>{author.first_name} {author.last_name} <br /></span>
					{/each}</td
				>
				<td>{submission.title}</td>
				<td>{submission.topic.name}</td>
				<td>{submission.presentation_format}</td>
				<td>{new Date(submission.created_at).toLocaleString()}</td>
				<td
					><a href="/submission/{submission.id}"
						><Icon class="icon" icon="material-symbols-light:search" /></a
					></td
				>
				<td>
					<div style="display: flex; align-items: center; justify-content: center;">
						<select
							on:change={(elem) => {
								setStatus(submission.id, elem.target.value);
							}}
							style="width:150px; margin:0"
							name="pets"
							id="pet-select"
						>
							{#each Object.keys(review_statuses) as status}
								<option selected={status == submission.review_result} value={status}>
									{review_statuses[status]}
								</option>
							{/each}
						</select>
					</div>
				</td>
			</tr>
		{/each}
	</table>
</div>
