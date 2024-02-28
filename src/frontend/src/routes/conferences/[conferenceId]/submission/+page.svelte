<script>
	import { page } from '$app/stores';
	import { onMount } from 'svelte';
	import { countries } from 'countries-list';

	export let data;
	const countryCodes = Object.keys(countries);
	const countryNames = countryCodes.map((code) => countries[code].name);

	let conferenceData = data.conference;
	let topics = conferenceData.topics;
	let authors = [];
	let abstractLength = 0;
	let keywordsLength = 0;
	function handleAbstractChange(event) {
		abstractLength = event.target.value.trim().split(/\s+/).length;
	}
	function handleKeyWordsChange(event) {
		keywordsLength = event.target.value.split(/\r\n|\r|\n/).length;
	}
	function addAuthor() {
		authors.push({
			id: authors.length,
			first_name: '',
			last_name: '',
			surname: '',
			email: '',
			country: '',
			affilation: '',
			web_page: '',
			is_presenter: false
		});
		authors = authors;
	}
	onMount(async () => {
		addAuthor();
	});
	function deleteAuthor(id) {
		let new_authors = [];
		for (let author of authors) {
			if (author.id != id) new_authors.push(author);
		}
		authors = new_authors;
	}
	function handleOnSubmit(event) {
		if (keywordsLength < 3) {
			event.preventDefault();
			alert('You should specify at least three keywords');
			return;
		}
		if (abstractLength > 100) {
			event.preventDefault();
			alert('Abstract should not exceed 100 words');
			return;
		}
		if (authors.length == 0) {
			event.preventDefault();
			alert('Please add at least one author');
			return;
		}
	}
</script>

<div class="container">
	<div class="form-wrapper">
		<form id="submission" on:submit={handleOnSubmit} method="POST">
			<input
				class="add_new_author-button"
				type="button"
				on:click={addAuthor}
				value="Add new author"
			/>
			<div class="authors-container">
				{#each authors as author}
					<article class="author-item">
						<label>
							First name*
							<input
								type="text"
								on:input={(author.first_name = this.value)}
								placeholder="First name"
								name="#{author.id}#_first_name"
								required
								value={author.first_name}
							/>
						</label>
						<label>
							Last name*
							<input
								type="text"
								on:input={(author.last_name = this.value)}
								placeholder="Last name"
								name="#{author.id}#_last_name"
								required
								value={author.last_name}
							/>
						</label>
						<label>
							Surname
							<input
								type="text"
								on:input={(author.surname = this.value)}
								placeholder="Surname"
								name="#{author.id}#_surname"
								value={author.surname}
							/>
						</label>
						<label>
							Email*
							<input
								type="email"
								on:input={(author.email = this.value)}
								placeholder="Email"
								name="#{author.id}#_email"
								required
								value={author.email}
							/>
						</label>

						<label>
							Country*
							<select
								required
								placeholder="Country"
								name="#{author.id}#_country"
								on:change={(author.country = this.value)}
							>
								<option value="" selected disabled>Country</option>
								{#each countryNames as country}
									<option value={country}>{country}</option>
								{/each}
							</select>
						</label>
						<label>
							Affilation*
							<input
								type="text"
								on:input={(author.affilation = this.value)}
								placeholder="Affilation"
								name="#{author.id}#_affilation"
								required
								value={author.affilation}
							/>
						</label>
						<label>
							Web page
							<input
								type="text"
								on:input={(author.web_page = this.value)}
								placeholder="Web page"
								name="#{author.id}#_web_page"
								value={author.web_page}
							/>
						</label>
						<label class="is_presenter-label">
							Is presenter
							<input
								type="checkbox"
								on:input={(author.is_presenter = this.checked)}
								placeholder="Is presenter"
								name="#{author.id}#_is_presenter"
								value={author.is_presenter}
							/>
						</label>
						<input type="button" on:click={deleteAuthor(author.id)} value="Delete" />
					</article>
				{/each}
			</div>
			<label>
				Title*
				<input type="text" placeholder="Title" name="title" required />
			</label>
			<label>
				Abstract*
				<p><i>The abstract should not exceed 100 words</i></p>
				<textarea
					on:change={handleAbstractChange}
					name="abstract"
					form="submission"
					cols="30"
					rows="10"
				></textarea>
				<p><b>Words: {abstractLength}</b></p>
			</label>
			<label>
				Keywords*
				<p>
					<i
						>Type a list of keywords (also known as key phrases or key terms), one per line to
						characterize your submission. You should specify at least three keywords.
					</i>
				</p>

				<textarea
					on:change={handleKeyWordsChange}
					name="keywords"
					form="submission"
					cols="30"
					rows="10"
				></textarea>
				<p><b>Keywords: {keywordsLength}</b></p>
			</label>
			<label>
				Topics*
				<select name="topic">
					{#each topics as topic}
						<option value={topic.id}>{topic.name}</option>
					{/each}
				</select>
			</label>
			<label>
				Presentation format*
				<select name="presentation_format">
					<option value="online" selected>Online</option>
					<option value="offline">On-Sight</option>
				</select>
			</label>

			<input class="floating-button" type="submit" value="Submit" />
		</form>
	</div>
</div>

<style>
	.add_new_author-button {
		width: 200px;
	}
	.authors-container {
		display: flex;
		gap: 20px;
		flex-wrap: wrap;
		justify-content: space-evenly;
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
		width: 250px;
	}

	.is_presenter-label > input {
		width: 40px !important;
		height: 40px !important;
	}
</style>
