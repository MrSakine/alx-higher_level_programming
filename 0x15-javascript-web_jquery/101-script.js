$(function () {
  const lists = $('ul.my_list');
  const add = $('div#add_item');
  const remove = $('div#remove_item');
  const clear = $('div#clear_list');

  add.on('click', function () {
    lists.append('<li>Item</li>');
  });

  remove.on('click', function () {
    $('ul li:last-child').remove();
  });

  clear.on('click', function () {
    lists.empty();
  });
});
