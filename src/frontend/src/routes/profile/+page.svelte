<script>
	import Icon from '@iconify/svelte';
	import { review_statuses } from '../../utils';
	export let data;
	let submissions = data.profile.submissions;
	let categories = {};
	submissions.forEach((element) => {
		if (categories[element.conference.name] == undefined)
			categories[element.conference.name] = [element];
		else categories[element.conference.name].push(element);
	});
	function joinAuthors(submission) {
		let authors = [];
		submission.authors.forEach((element) =>
			authors.push(element.first_name + ' ' + element.last_name)
		);
		return authors.join();
	}
	function convertAuthors(authors) {
		let res = [];
		authors.forEach((element) => {
			res.push(`${element.first_name} ${element.last_name}`);
		});
		return res;
	}
</script>

<svelte:head>
	<title>Author</title>
	<meta name="description" content="Registration page" />
</svelte:head>

<div class="container">
	<h4>Author Profile</h4>

	<a href="/profile/edit">Edit</a>

	<table class="profile_info-container">
		<tr class="profile_info-row">
			<td class="profile_info-name">Title</td>
			<td class="profile_info-data">{data.profile.title != null ? data.profile.title : ''}</td>
		</tr>
		<tr class="profile_info-row">
			<td class="profile_info-name">First name</td>
			<td class="profile_info-data"
				>{data.profile.first_name != null ? data.profile.first_name : ''}</td
			>
		</tr>
		<tr class="profile_info-row">
			<td class="profile_info-name">Last name:</td>
			<td class="profile_info-data"
				>{data.profile.last_name != null ? data.profile.last_name : ''}</td
			>
		</tr>
		<tr class="profile_info-row">
			<td class="profile_info-name">Surname:</td>
			<td class="profile_info-data">{data.profile.surname != null ? data.profile.surname : ''}</td>
		</tr>
		<tr class="profile_info-row">
			<td class="profile_info-name">Affiliation:</td>
			<td class="profile_info-data"
				>{data.profile.affilation != null ? data.profile.affilation : ''}</td
			>
		</tr>

		<tr class="profile_info-row">
			<td class="profile_info-name">Country:</td>
			<td class="profile_info-data">{data.profile.country != null ? data.profile.country : ''}</td>
		</tr>
		<tr class="profile_info-row">
			<td class="profile_info-name">City:</td>
			<td class="profile_info-data">{data.profile.city != null ? data.profile.city : ''}</td>
		</tr>
		<tr class="profile_info-row">
			<td class="profile_info-name">State:</td>
			<td class="profile_info-data">{data.profile.state != null ? data.profile.state : ''}</td>
		</tr>
		<tr class="profile_info-row">
			<td class="profile_info-name">ORCID ID:</td>
			<td class="profile_info-data">{data.profile.orcid_id != null ? data.profile.orcid_id : ''}</td
			>
		</tr>
		<tr class="profile_info-row">
			<td class="profile_info-name">Web page:</td>
			<td class="profile_info-data">{data.profile.web_page != null ? data.profile.web_page : ''}</td
			>
		</tr>
	</table>
	<h4>My Submissions</h4>
	{#if submissions.length}
		<div>
			{#each Object.keys(categories) as category}
				<details>
					<summary>{category}</summary>
					<table class="striped conferences-table">
						<thead>
							<td>
								<button class="bare_button">#</button>
							</td>
							<td><button class="bare_button">Authors</button></td>
							<td>
								<button class="bare_button">Title</button>
							</td>
							<td>
								<button class="bare_button">Topic</button>
							</td>
							<td>
								<button class="bare_button">Report Format</button>
							</td>
							<td>
								<button class="bare_button">Submitted At</button>
							</td>
							<td><button class="bare_button">View</button></td>
							<td>
								<button class="bare_button">Review status</button>
							</td>
						</thead>
						<tbody>
							{#each categories[category] as submission}
								<tr>
									<td class="centered id-column">{submission.id}</td>
									<td style="width: 100px">
										{convertAuthors(submission.authors)}
									</td>
									<td style="width: 400px">{submission.title}</td>
									<td class="centered">{submission.topic.name}</td>
									<td class="centered">{submission.presentation_format}</td>
									<td class="centered">{new Date(submission.created_at).toLocaleString()}</td>
									<td class="centered">
										<a href="/submission/{submission.id}"
											><Icon class="icon" icon="material-symbols-light:search" /></a
										></td
									>
									<td>
										<div style="display: flex; align-items: center; justify-content: center;">
											{review_statuses[submission.review_result]}
										</div>
									</td>
								</tr>
							{/each}
						</tbody>
					</table>
				</details>
			{/each}
		</div>
	{:else}
		<p>There are no submissions yet.</p>
		<a href="/conferences">Make a new submission</a>
	{/if}
</div>

<style>
	summary {
		max-width: fit-content;
	}
	.profile_info-container {
		max-width: 450px;
	}
	.conferences-table * {
		font-size: 16px;
		padding: 10px;
	}
	.conferences-table > thead * {
		text-align: center;
	}
	table > thead * {
		padding: 0 !important;
	}
</style>
