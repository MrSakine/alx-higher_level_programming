$(function () {
  const input = $('input#language_code');
  const btn = $('input#btn_translate');
  const hello = $('div#hello');

  btn.on('click', function () {
    getData();
  });

  input.on('keypress', function (e) {
    if (e.which === 13) {
      getData();
    }
  });

  function getData () {
    const temp = input.val().toLowerCase();
    hello.text('Fetching data...');
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${temp}`, (res) => {
      hello.text(res.hello);
    });
  }
});
