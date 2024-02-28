$(function () {
  $('div#hello').text('Fetching data...');
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (res) => {
    $('div#hello').text(res.hello);
  });
});
