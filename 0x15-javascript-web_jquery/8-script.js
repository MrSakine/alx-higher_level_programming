$('ul#list_movies').text('Fetching data...');
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (res) => {
  $('ul#list_movies').empty();
  for (const data of res.results) {
    $('ul#list_movies').append(`<li>${data.title}</li>`);
  }
});
