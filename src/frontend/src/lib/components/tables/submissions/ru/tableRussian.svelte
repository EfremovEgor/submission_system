<script>
	import { review_statuses, review_statuses_ru } from '../../../../../utils';
	import Icon from '@iconify/svelte';
	export let to_display;
	export let canReview;
	export let data;
	export let setStatus;
	let categories = {};
	let checked_topics = {};

	data.conference.topics.forEach((element) => {
		let topic = element;
		if (categories[topic.category_ru] == null) categories[topic.category_ru] = [];
		if (!categories[topic.category_ru].includes(topic.name_ru))
			categories[topic.category_ru].push(topic.name_ru);
	});
	Object.values(categories).forEach((element) => {
		element.forEach((topic) => {
			checked_topics[topic] = true;
		});
	});
	function count_submissions(topic) {
		let counter = 0;
		data.submissions.forEach((element) => {
			if (element.topic.name_ru == topic) counter++;
		});
		return counter;
	}
	function filterSubmissions() {
		to_display = [];
		data.submissions.forEach((element) => {
			if (checked_topics[element.topic.name_ru]) {
				to_display.push(element);
			}
		});
	}

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

	function convertAuthors(authors) {
		let res = [];
		authors.forEach((element) => {
			res.push(
				`${element.first_name_ru != null ? element.first_name_ru : element.first_name} ${element.last_name_ru != null ? element.last_name_ru : element.last_name}`
			);
		});
		return res;
	}
</script>

<details open>
	<summary style="width: fit-content;">Выберите направление</summary>
	<div style="max-width: 700px;">
		{#each Object.keys(categories) as category}
			<tr>
				<details>
					<summary style="width: fit-content;">{category}</summary>
					<table class="striped">
						<tbody>
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
									<td style="padding-left: 10px;">{count_submissions(topic)}</td>
								</tr>
							{/each}
						</tbody>
					</table>
				</details></tr
			>
		{/each}
	</div>
</details>
<span>Показано: {to_display.length}/{data.submissions.length} <br /></span>
<button style="padding:0" class="bare_button">Экспортировать в Excel</button>
<div class="overflow-auto">
	<table class="striped content">
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
			<td><button class="bare_button">Авторы</button></td>
			<td>
				<button
					on:click={(element) => {
						let order = parseInt(element.target.order);
						if (isNaN(order)) order = 1;
						sortSubmissions(element.target.name, order);
						element.target.order = -order;
					}}
					name="title"
					class="bare_button">Название</button
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
					class="bare_button">Направление</button
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
					class="bare_button">Формат доклада</button
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
					class="bare_button">Подано</button
				>
			</td>
			<td><button class="bare_button">Просмотр</button></td>
			<td>
				<button
					on:click={(element) => {
						let order = parseInt(element.target.order);
						if (isNaN(order)) order = 1;
						sortSubmissions(element.target.name, order);
						element.target.order = -order;
					}}
					name="review_result"
					class="bare_button">Статус</button
				>
			</td>
		</thead>
		{#each to_display as submission}
			<tr>
				<td class="centered id-column">{submission.id}</td>
				<td style="width: 100px">
					{convertAuthors(submission.authors).join(', ')}
				</td>
				<td style="width: 400px">{submission.title_ru ? submission.title_ru : submission.title}</td>
				<td class="centered"
					>{submission.topic.name_ru ? submission.topic.name_ru : submission.topic.name}</td
				>
				<td class="centered">{submission.presentation_format == 'online' ? 'заочный' : 'очный'}</td>
				<td class="centered">{new Date(submission.created_at).toLocaleString()}</td>
				<td class="centered">
					<a href="/submission/{submission.id}"
						><Icon class="icon" icon="material-symbols-light:search" /></a
					>
				</td>

				<td class="centered">
					{#if canReview}
						<div style="display: flex; align-items: center; gap:10px">
							<select bind:this={submission.status_select} style="width:150px; margin:0">
								{#each Object.keys(review_statuses_ru) as status}
									<option selected={status == submission.review_result} value={status}>
										{review_statuses_ru[status]}
									</option>
								{/each}
							</select>
							<button
								on:click={() => {
									setStatus(submission.id, submission.status_select.value);
								}}
								class="icon-button2"
							>
								<Icon
									icon="carbon:checkmark-outline"
									style="padding:0; cursor: pointer;    color: var(--pico-primary);"
									width="40"
									height="40"
								/></button
							>
						</div>
					{:else}
						{review_statuses_ru[submission.review_result]}
					{/if}
				</td>
			</tr>
		{/each}
	</table>
</div>

<style>
	table *,
	details > div * {
		font-size: 16px;
	}
	.centered,
	thead * {
		text-align: center;
	}
	table > thead * {
		padding: 0 !important;
	}
	details > div * {
		padding: 0;
	}
	table * {
		padding: 10px;
	}
	.id-column {
		width: 20px;
	}
</style>
