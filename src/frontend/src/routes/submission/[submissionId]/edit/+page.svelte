<script>
	import RussianSubmissionForm from '$components/forms/russianSubmissionEditForm/russianSubmissionEditForm.svelte';
	import EnglishSubmitForm from '$components/forms/englishSubmissionEditForm/englishSubmissionEditForm.svelte';
	import { onMount } from 'svelte';
	import { countries } from 'countries-list';

	export let data;

	const userDetails = data.userDetails;
	const countryCodes = Object.keys(countries);
	const countryNames = countryCodes.map((code) => countries[code].name);
	let modal;
	let languageChoose;
	let isBusy = false;
	let sentEmail = false;
	let submissionData = data.submission;
	let conferenceData = data.conference;
	let categories = {};
	conferenceData.topics.forEach((element) => {
		if (categories[element.category] == undefined) categories[element.category] = [element];
		else categories[element.category].push(element);
	});
	let authors = [];

	function handleFillAuthorForm(id) {
		authors[id].first_name = userDetails.first_name;
		authors[id].title = userDetails.title;
		authors[id].last_name = userDetails.last_name;
		authors[id].surname = userDetails.surname;
		authors[id].email = userDetails.email;
		authors[id].country = userDetails.country;
		authors[id].affilation = userDetails.affilation;
		authors[id].web_page = userDetails.web_page;
	}
	function handlePresentationFormatChange(event) {
		presentationFormat = event.target.value;
	}
	function handleAbstractChange(event) {
		abstractLength = event.target.value.trim().split(/\s+/).length;
	}
	function handleKeyWordsChange(event) {
		keywordsLength = event.target.value.split(/\r\n|\r|\n/).length;
	}
	function addAuthor() {
		authors.push({
			id: authors.length,
			title: '',
			first_name: '',
			last_name: '',
			first_name_ru: '',
			last_name_ru: '',
			surname: '',
			surname_ru: '',
			email: '',
			country: '',
			affilation: '',
			affilation_ru: '',
			web_page: '',
			is_presenter: false,
			is_corresponding: false
		});
		authors = authors;
	}
	onMount(async () => {
		addAuthor();
		addAuthor();
		if (!conferenceData.allow_ru || conferenceData.allow_ru == null) {
			is_ru = false;
		}
	});
</script>

<svelte:head>
	<title>Submission {conferenceData.short_name}</title>
	<meta name="description" content="Home" />
</svelte:head>
<div class="container">
	{#if isBusy}
		<article aria-busy="true">Please wait while we are processing your submission...</article>
	{:else if sentEmail}
		<article class="verification_sent-container">
			<h3>Your paper was successfully edited</h3>
		</article>
	{:else}
		{#if submissionData.is_ru == true}
			<h3>Изменение доклада #{submissionData.id} на {conferenceData.name_ru_dative}</h3>
		{:else}
			<h3>New Submission for {conferenceData.short_name}</h3>
		{/if}
		{#if submissionData.is_ru == true}
			<RussianSubmissionForm
				bind:isBusy
				bind:sentEmail
				{userDetails}
				{submissionData}
				{conferenceData}
			/>
		{:else}
			<EnglishSubmitForm
				bind:isBusy
				bind:sentEmail
				{userDetails}
				{submissionData}
				{conferenceData}
			/>
		{/if}
	{/if}
</div>

<style>
	.verification_sent-container {
		margin: auto;
		width: fit-content;
		min-height: 300px;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	.verification_sent-container > h3 {
		color: rgb(71, 164, 23);
	}

	.modal {
		width: fit-content;
	}
	.modal > footer {
		display: flex;
		justify-content: center;
		align-items: center;
	}
	.modal > footer > button {
		min-width: 120px;
	}
	.modal-main {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
	.add_new_author-button,
	.submit-button {
		width: 200px;
	}
	.authors-container {
		display: flex;
		gap: 20px;
		flex-wrap: wrap;
	}
	.author-item {
		padding: 20px;
	}
	.author-item > label {
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: center;
		gap: 20px;
	}
	.author-item > label > input,
	select {
		width: 200px;
	}
	.author-item {
		min-width: 400px;
	}
	.ru_author > label {
		display: flex;
		flex-flow: row;
	}

	.ru_author > label > * {
		width: 200px;
	}
	.is_presenter-label,
	.is_corresponding-label {
		width: 100%;
		align-items: center;
		justify-content: center !important;
		flex-direction: row !important;
	}
	.delete_author-button {
		width: 40px;
		padding: 0px;
		height: 40px;
		margin: 0;
	}

	.delete_author-container {
		display: flex;
		width: 100%;
		justify-content: end;
		min-height: 50px;
	}
</style>
