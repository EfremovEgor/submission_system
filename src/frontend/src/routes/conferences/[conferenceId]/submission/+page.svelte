<script>
	import { page } from '$app/stores';
	export let data;
	let conferenceData = data.conference;
	let topics = conferenceData.topics;
	let authors = [];

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
	function deleteAuthor(id) {
		let new_authors = [];
		for (let author of authors) {
			if (author.id != id) new_authors.push(author);
		}
		authors = new_authors;
	}
	function handleOnSubmit(event) {
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
			<div class="authors-container">
				<input type="button" on:click={addAuthor} value="Add new author" />
				{#each authors as author}
					<div class="author-item">
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
							<input
								type="text"
								on:input={(author.country = this.value)}
								placeholder="Country"
								name="#{author.id}#_country"
								required
								value={author.country}
							/>
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
						<label>
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
					</div>
				{/each}
			</div>
			<label>
				Title*
				<input type="text" placeholder="Title" name="title" required />
			</label>
			<label>
				Abstract*
				<textarea name="abstract" form="submission" cols="30" rows="10"></textarea>
			</label>
			<label>
				Keywords*
				<textarea name="keywords" form="submission" cols="30" rows="10"></textarea>
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
					<option value="offline">Offline</option>
				</select>
			</label>

			<input class="floating-button" type="submit" value="Submit" />
		</form>
	</div>
</div>

<style>
	.form-wrapper {
		max-width: 400px;
	}
</style>
