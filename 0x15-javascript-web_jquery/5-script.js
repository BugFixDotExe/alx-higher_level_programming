$('DIV#add_item').on('click', function () {
  const item1 = $('<li></li>').text('Item');
  $('UL.my_list').append(item1);
});
