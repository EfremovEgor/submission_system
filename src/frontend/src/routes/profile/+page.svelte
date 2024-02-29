<script>
	export let data;
</script>

<svelte:head>
	<title>Author</title>
	<meta name="description" content="Registration page" />
</svelte:head>

<div class="container">
	<h3>Author</h3>
	<table class="profile_info-container">
		<tr class="profile_info-row">
			<td class="profile_info-name">First name</td>
			<td class="profile_info-data"
				>{data.profile.first_name != null ? data.profile.first_name : 'No data'}</td
			>
		</tr>
		<tr class="profile_info-row">
			<td class="profile_info-name">Last name:</td>
			<td class="profile_info-data"
				>{data.profile.last_name != null ? data.profile.last_name : 'No data'}</td
			>
		</tr>
		<tr class="profile_info-row">
			<td class="profile_info-name">Surname:</td>
			<td class="profile_info-data"
				>{data.profile.surname != null ? data.profile.surname : 'No data'}</td
			>
		</tr>
		<tr class="profile_info-row">
			<td class="profile_info-name">Affilation:</td>
			<td class="profile_info-data"
				>{data.profile.affilation != null ? data.profile.affilation : 'No data'}</td
			>
		</tr>
		<tr class="profile_info-row">
			<td class="profile_info-name">Web page:</td>
			<td class="profile_info-data"
				>{data.profile.web_page != null ? data.profile.web_page : 'No data'}</td
			>
		</tr>
		<tr class="profile_info-row">
			<td class="profile_info-name">Address line 1:</td>
			<td class="profile_info-data"
				>{data.profile.address_line_1 != null ? data.profile.address_line_1 : 'No data'}</td
			>
		</tr>
		<tr class="profile_info-row">
			<td class="profile_info-name">Address line 2:</td>
			<td class="profile_info-data"
				>{data.profile.surname != null ? data.profile.surname : 'No data'}</td
			>
		</tr>
		<tr class="profile_info-row">
			<td class="profile_info-name">City:</td>
			<td class="profile_info-data">{data.profile.city != null ? data.profile.city : 'No data'}</td>
		</tr>
		<tr class="profile_info-row">
			<td class="profile_info-name">State:</td>
			<td class="profile_info-data"
				>{data.profile.state != null ? data.profile.state : 'No data'}</td
			>
		</tr>
		<tr class="profile_info-row">
			<td class="profile_info-name">Country:</td>
			<td class="profile_info-data"
				>{data.profile.country != null ? data.profile.country : ''}</td
			>
		</tr>
	</table>
	<a role="button" class="blue-button outline edit_author-button" href="/profile/edit">Edit</a>
	<h3>Submissions</h3>
	<table class="submissions_table">
		<thead>
			<th>Title</th>
			<th>Approved</th>
		</thead>
		{#each data.profile.submissions as submission}
			<tr>
				<td>
					{submission.title}
				</td>
				<td>
					{submission.approved}
				</td>
			</tr>
		{/each}
	</table>
</div>

<style>
	.edit_author-button {
		min-width: 150px;
		margin: auto;
	}
	.profile_info-container,
	.submissions_table {
		max-width: 450px;
	}
</style>
