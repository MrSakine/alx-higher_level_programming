$('div#character').text('Fetching data...');
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data) => {
  $('div#character').text(data.name);
});
