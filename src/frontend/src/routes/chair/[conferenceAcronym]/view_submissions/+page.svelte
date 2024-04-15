<script>
	export let data;
	import TableEnglish from '$components/tables/submissions/en/tableEnglish.svelte';
	import TableRussian from '$components/tables/submissions/ru/tableRussian.svelte';
	let to_display = data.submissions;
	let isRu = false;

	async function setStatus(id, status) {
		const response = await fetch('/api/submissions/setStatus', {
			method: 'POST',
			body: JSON.stringify({ id: id, review_result: status }),
			headers: {
				'content-type': 'application/json'
			}
		});
	}
</script>

<svelte:head>
	<title>Chair</title>
	<meta name="description" content="Chair" />
</svelte:head>
<div class="container">
	<div class="heading-nav">
		<label>
			Eng
			<input
				bind:checked={isRu}
				style="background-color: var(--pico-primary); border-color: var(--pico-primary); margin: 0;"
				name="terms"
				type="checkbox"
				role="switch"
			/>
			Rus
		</label>
		<h3>{data.conference.name}</h3>
	</div>

	{#if isRu}
		<TableRussian {setStatus} {data} {to_display} canReview={false} />
	{:else}
		<TableEnglish {setStatus} {data} {to_display} canReview={false} />
	{/if}
</div>
