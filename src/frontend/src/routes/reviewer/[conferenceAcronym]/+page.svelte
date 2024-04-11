<script>
	export let data;
	import { review_statuses } from '../../../utils';

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
			if (checked_topics[element.topic.name]) {
				to_display.push(element);
			}
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
		element.forEach((topic) => {
			checked_topics[topic] = true;
		});
	});
	function sortSubmissions(field, order) {
		function compare(a, b) {
			let compareBy = field;
			if (compareBy == 'topic') {
				a = a[compareBy];
				b = b[compareBy];
				console.log(a, b);

				compareBy = 'name';
			}

			if (a[compareBy] < b[compareBy]) {
				return -1;
			}
			if (a[compareBy] < b[compareBy]) {
				return 1;
			}
			return 0;
		}
		to_display.sort(compare);
		if (order == -1) to_display.reverse();
		to_display = to_display;
	}
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
			<td>
				<button
					on:click={(element) => {
						let order = parseInt(element.target.order);
						if (isNaN(order)) order = 1;
						sortSubmissions(element.target.name, order);
						element.target.order = -order;
					}}
					name="id"
					class="bare_button">#</button
				>
			</td>
			<td>Authors</td>
			<td>
				<button
					on:click={(element) => {
						let order = parseInt(element.target.order);
						if (isNaN(order)) order = 1;
						sortSubmissions(element.target.name, order);
						element.target.order = -order;
					}}
					name="title"
					class="bare_button">Title</button
				>
			</td>
			<td>
				<button
					on:click={(element) => {
						let order = parseInt(element.target.order);
						if (isNaN(order)) order = 1;
						sortSubmissions(element.target.name, order);
						element.target.order = -order;
					}}
					name="topic"
					class="bare_button">Topic</button
				>
			</td>
			<td>
				<button
					on:click={(element) => {
						let order = parseInt(element.target.order);
						if (isNaN(order)) order = 1;
						sortSubmissions(element.target.name, order);
						element.target.order = -order;
					}}
					name="presentation_format"
					class="bare_button">Report Format</button
				>
			</td>
			<td>
				<button
					on:click={(element) => {
						let order = parseInt(element.target.order);
						if (isNaN(order)) order = 1;
						sortSubmissions(element.target.name, order);
						element.target.order = -order;
					}}
					name="created_at"
					class="bare_button">Created At</button
				>
			</td>
			<td>View</td>
			<td>
				<button
					on:click={(element) => {
						let order = parseInt(element.target.order);
						if (isNaN(order)) order = 1;
						sortSubmissions(element.target.name, order);
						element.target.order = -order;
					}}
					name="review_result"
					class="bare_button">Review status</button
				>
			</td>
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
