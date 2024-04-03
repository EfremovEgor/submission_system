<script>
	import Icon from '@iconify/svelte';
	export let data;
	let submission = data.submission;
	let deleteDialogOpen = false;
</script>

<svelte:head>
	<title>Submission {submission.id}</title>
	<meta name="description" content="Submission {submission.id}" />
</svelte:head>

<div class="container">
	<dialog open={deleteDialogOpen}>
		<article class="modal">
			<header>
				<p>
					<strong> Submission {submission.id}</strong>
				</p>
			</header>
			<div>
				<p>
					<strong>Do you want to delete Submission #{submission.id}</strong>
				</p>
			</div>
			<footer>
				<form method="POST">
					<button class="button-error">Delete</button>
				</form>
				<button
					on:click={(event) => {
						deleteDialogOpen = false;
					}}>Cancel</button
				>
			</footer>
		</article>
	</dialog>
	<h4>{submission.conference.short_name} Submission #{submission.id}</h4>
	<div class="actions">
		<button class="bare_button"
			><a style="text-decoration: none;" href="/submission/{submission.id}/edit">Edit</a></button
		>
		<button on:click={() => (deleteDialogOpen = true)} class="bare_button bare_button-error"
			>Delete</button
		>
	</div>
	<table>
		<tbody>
			<tr>
				<td> Title </td>
				<td>
					{submission.title}
				</td>
			</tr>
			<tr>
				<td> Keywords </td>
				<td>
					{#each submission.keywords.split('\n') as keyword}
						<span>{keyword} <br /></span>
					{/each}
				</td>
			</tr>
			<tr>
				<td> Topic </td>
				<td>
					{submission.topic.name}
				</td>
			</tr>
			<tr>
				<td> Abstract </td>
				<td>
					{submission.abstract}
				</td>
			</tr>
			<tr>
				<td> Submitted </td>
				<td>
					{new Date(submission.created_at).toLocaleString()}
				</td>
			</tr>
			<tr>
				<td> Important Notice </td>
				<td> I confirm that my manuscript can be published </td>
			</tr>
			<tr>
				<td> Presentation Format </td>
				<td
					>{submission.presentation_format.charAt(0).toUpperCase() +
						submission.presentation_format.slice(1)}</td
				>
			</tr>
		</tbody>
	</table>

	<h4>Authors</h4>

	<div class="overflow-auto">
		<table class="striped authors-table">
			<thead>
				<tr>
					<th scope="col">First name</th>
					<th scope="col">Last name</th>
					<th scope="col">Email</th>
					<th scope="col">Country</th>
					<th scope="col">Affiliation</th>
					<th scope="col">Corresponding</th>
					<th scope="col">Presenter</th>
				</tr>
			</thead>
			<tbody>
				{#each submission.authors as author}
					<tr>
						<td>{author.first_name}</td>
						<td>{author.last_name}</td>
						<td>{author.email}</td>
						<td>{author.country}</td>
						<td>{author.affilation}</td>
						<td
							>{#if author.is_corresponding}
								<div><Icon icon="ion:checkmark" /></div>
							{/if}</td
						>
						<td
							>{#if author.is_presenter}
								<div><Icon icon="ion:checkmark" /></div>
							{/if}</td
						></tr
					>
				{/each}
			</tbody>
		</table>
	</div>
</div>

<style>
	.modal > footer {
		display: flex;
		gap: 30px;
		width: 100%;
		justify-content: end;
	}
	.authors-table > * > * > td,
	th {
		width: fit-content;
		text-align: center;
	}
	.actions {
		display: flex;
		gap: 20px;
	}
</style>
