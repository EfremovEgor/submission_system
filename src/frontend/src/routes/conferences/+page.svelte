<script>
	export let data;
	let conferences = data.conferences;
	import { convertToDate } from '../../utils';
</script>

<svelte:head>
	<title>Call For Papers</title>
	<meta name="description" content="Call For Papers" />
</svelte:head>

<div class="container">
	<h3>Call For Papers</h3>
	{#if conferences.length}
		<table class="striped conferences-wrapper">
			<thead>
				<tr>
					<th scope="col">Short Name</th>
					<th scope="col">Name</th>
					<th scope="col">Submission deadline</th>
					<th scope="col">Start date</th>
				</tr>
			</thead>
			<tbody>
				{#each conferences as conference}
					<tr class="conference-container">
						<td
							><a class="conference_page-button" href="/conferences/{conference.acronym}"
								>{conference.short_name}</a
							></td
						>
						<td> {conference.name}</td>
						<td>
							{conference.submission_deadline != null
								? convertToDate(conference.submission_deadline)
								: ''}
						</td>
						<td
							>{conference.start_date != null ? convertToDate(conference.start_date) : ''}
						</td></tr
					>
				{/each}
			</tbody>
		</table>
	{:else}
		<p aria-busy="true">Please wait while we are searching for available conferences</p>
	{/if}
</div>

<style>
</style>
