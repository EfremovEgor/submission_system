<script>
	export let data;
</script>

<svelte:head>
	<title>Profile</title>
	<meta name="description" content="Registration page" />
</svelte:head>

<div class="container">
	<div class="profile_info-container">
		<div class="profile_info-row">
			<span class="profile_info-name">First name:</span>
			<span class="profile_info-data"
				>{data.profile.first_name != null ? data.profile.first_name : 'No data'}</span
			>
		</div>
		<div class="profile_info-row">
			<span class="profile_info-name">Last name:</span>
			<span class="profile_info-data"
				>{data.profile.last_name != null ? data.profile.last_name : 'No data'}</span
			>
		</div>
		<div class="profile_info-row">
			<span class="profile_info-name">Surname:</span>
			<span class="profile_info-data"
				>{data.profile.surname != null ? data.profile.surname : 'No data'}</span
			>
		</div>
		<div class="profile_info-row">
			<span class="profile_info-name">Affilation:</span>
			<span class="profile_info-data"
				>{data.profile.affilation != null ? data.profile.affilation : 'No data'}</span
			>
		</div>
		<div class="profile_info-row">
			<span class="profile_info-name">Web page:</span>
			<span class="profile_info-data"
				>{data.profile.web_page != null ? data.profile.web_page : 'No data'}</span
			>
		</div>
		<div class="profile_info-row">
			<span class="profile_info-name">Address line 1:</span>
			<span class="profile_info-data"
				>{data.profile.address_line_1 != null ? data.profile.address_line_1 : 'No data'}</span
			>
		</div>
		<div class="profile_info-row">
			<span class="profile_info-name">Address line 2:</span>
			<span class="profile_info-data"
				>{data.profile.surname != null ? data.profile.surname : 'No data'}</span
			>
		</div>
		<div class="profile_info-row">
			<span class="profile_info-name">City:</span>
			<span class="profile_info-data"
				>{data.profile.city != null ? data.profile.city : 'No data'}</span
			>
		</div>
		<div class="profile_info-row">
			<span class="profile_info-name">State:</span>
			<span class="profile_info-data"
				>{data.profile.state != null ? data.profile.state : 'No data'}</span
			>
		</div>
		<div class="profile_info-row">
			<span class="profile_info-name">Country:</span>
			<span class="profile_info-data"
				>{data.profile.country != null ? data.profile.country : 'No data'}</span
			>
		</div>
	</div>
	<a href="/profile/edit">Edit</a>
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
	.submissions_table {
		max-width: 450px;
	}
</style>
