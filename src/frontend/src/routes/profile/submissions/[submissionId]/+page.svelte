<script>
	export let data;
    console.log(data.submission)
    let authors = [];
    data.submission.authors.forEach(element => {
        authors.push({
			id: authors.length,
			first_name: element.first_name,
			last_name: element.last_name,
			surname: element.surname,
			email: element.email,
			country: element.country,
			affilation: element.affilation,
			web_page: element.web_page,
			is_presenter: element.is_presenter
		});
    });
    console.log(authors)
</script>



<svelte:head>
	<title>Edit submission</title>
	<meta name="description" content="Registration page" />
</svelte:head>

<div class="container">
    {JSON.stringify(data.submission) }
</div>