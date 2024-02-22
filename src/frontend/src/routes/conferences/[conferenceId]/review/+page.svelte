<script>
	export let data;
</script>

<svelte:head>
	<title>Conference</title>
	<meta name="description" content="Home" />
</svelte:head>
<div class="container">
	<table class="striped">
		<thead>
			<td>#</td>
			<td>Authors</td>
			<td>Title</td>
			<td>Topic</td>
			<td>Report Format</td>
			<td>Approved</td>
			<td>Created At</td>
		</thead>
		{#each data.submissions as submission, i}
			<tr>
				<td>{i + 1}</td>
				<td
					>{#each submission.authors as author}
						<span>{author.first_name} {author.last_name}</span>
					{/each}</td
				>
				<td>{submission.title}</td>
				<td>{submission.topic.name}</td>
				<td>{submission.presentation_format}</td>
				<td>{submission.approved}</td>

				<td>{new Date(submission.created_at).toLocaleString()}</td>
			</tr>
		{/each}
	</table>
</div>
