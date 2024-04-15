<script>
	import Icon from '@iconify/svelte';
	export let data;
	let submission = data.submission;
	let deleteDialogOpen = false;
	let canEdit = false;
	if (data.user.id == submission.user_id) canEdit = true;
	data.user.reviewer_in.forEach((element) => {
		if (element.id == submission.conference.id) canEdit = true;
	});
	let isRu = false;
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
		<h4>{submission.conference.short_name} Submission #{submission.id}</h4>
	</div>
	{#if canEdit}
		<div class="actions">
			<button class="bare_button"
				><a style="text-decoration: none;" href="/submission/{submission.id}/edit"
					>{isRu ? 'Изменить' : 'Edit'}</a
				></button
			>
			<button on:click={() => (deleteDialogOpen = true)} class="bare_button bare_button-error"
				>{isRu ? 'Удалить' : 'Delete'}</button
			>
		</div>
	{/if}

	<table>
		<tbody>
			<tr>
				<td> {isRu ? 'Название' : 'Title'} </td>
				<td>
					{#if isRu && submission.title_ru}
						{submission.title_ru}
					{:else}
						{submission.title}
					{/if}
				</td>
			</tr>
			<tr>
				<td> {isRu ? 'Ключевые слова' : 'Keywords'} </td>
				<td>
					{#if isRu && submission.keywords_ru}
						{#each submission.keywords_ru.split('\n') as keyword}
							<span>{keyword} <br /></span>
						{/each}
					{:else}
						{#each submission.keywords.split('\n') as keyword}
							<span>{keyword} <br /></span>
						{/each}
					{/if}
				</td>
			</tr>
			<tr>
				<td> {isRu ? 'Направление' : 'Topic'} </td>
				<td>
					{#if isRu && submission.topic.name_ru}
						{submission.topic.name_ru}
					{:else}
						{submission.topic.name}
					{/if}
				</td>
			</tr>
			<tr>
				<td> {isRu ? 'Аннотация' : 'Abstract'} </td>
				<td>
					{#if isRu && submission.abstract_ru}
						{submission.abstract_ru}
					{:else}
						{submission.abstract}
					{/if}
				</td>
			</tr>
			<tr>
				<td> {isRu ? 'Подано' : 'Submitted'} </td>
				<td>
					{new Date(submission.created_at).toLocaleString()}
				</td>
			</tr>
			<tr>
				<td>{isRu ? 'Важное замечание' : 'Important Notice'} </td>
				<td
					>{isRu
						? 'Подтверждаю, что моя статья может быть опубликована'
						: 'I confirm that my manuscript can be published'}
				</td>
			</tr>
			<tr>
				<td>{isRu ? 'Формат доклада' : 'Presentation Format'} </td>
				<td>{submission.presentation_format}</td>
			</tr>
		</tbody>
	</table>

	<h4>{isRu ? 'Авторы' : 'Authors'}</h4>

	<div class="overflow-auto">
		<table class="striped authors-table">
			<thead>
				<tr>
					<th scope="col">{isRu ? 'Имя' : 'First name'} </th>
					<th scope="col">{isRu ? 'Фамилия' : 'Last name'} </th>
					<th scope="col">{isRu ? 'Почта' : 'Email'} </th>
					<th scope="col">{isRu ? 'Страна' : 'Country'} </th>
					<th scope="col">{isRu ? 'Организация' : 'Affiliation'} </th>
					<th scope="col">{isRu ? 'Контактное лицо' : 'Corresponding'} </th>
					<th scope="col">{isRu ? 'Докладчик' : 'Presenter'} </th>
				</tr>
			</thead>
			<tbody>
				{#each submission.authors as author}
					<tr>
						<td>
							{#if isRu && author.first_name_ru}
								{author.first_name_ru}
							{:else}
								{author.first_name}
							{/if}
						</td>
						<td>
							{#if isRu && author.last_name_ru}
								{author.last_name_ru}
							{:else}
								{author.last_name}
							{/if}
						</td>
						<td>{author.last_name}</td>
						<td>{author.email}</td>
						<td>
							{#if isRu && author.country}
								{author.country}
							{:else}
								{author.country}
							{/if}
						</td>
						<td>
							{#if isRu && author.affilation_ru}
								{author.affilation_ru}
							{:else}
								{author.affilation}
							{/if}
						</td>
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
