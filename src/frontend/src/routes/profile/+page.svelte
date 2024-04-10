<script>
	import Icon from '@iconify/svelte';
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
					<table class="striped conferences-wrapper">
						<thead>
							<tr>
								<th scope="col">Authors</th>
								<th scope="col">Title</th>
								<th scope="col">View</th>
								<th scope="col">Review Result</th>
							</tr>
						</thead>
						<tbody>
							{#each categories[category] as submission}
								<tr class="conference-container">
									<td>
										{#each submission.authors as author}
											<span>{joinAuthors(submission)}</span>
										{/each}</td
									>
									<td> {submission.title}</td>
									<td
										><a href="/submission/{submission.id}"
											><Icon class="icon" icon="material-symbols-light:search" /></a
										></td
									>
									<td> </td>
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
</style>
