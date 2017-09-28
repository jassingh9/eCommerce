$(document).ready(function(){
  $('#search_bar').submit(function(e){
  e.preventDefault()
  });
  $('#search_name').keyup(function(){
  $.ajax({
    url: '/search',
    method: 'post',
    data: $(this).parent().serialize(),
    success: function(serverResponse) {
      $('#allitems').html(serverResponse)
      }
    })
  });
  $(document).on('submit', '#search_bar_cat', function(e){
    e.preventDefault()
    $.ajax({
      url:$(this).attr('action'),
      method: 'post',
      data: $(this).serialize(),
      success: function(serverResponse) {
        $('#allitems').html(serverResponse)
      }
    })
  })
})
