var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on( 'connect', function() {
  socket.emit( 'order', {
    data: 'User Connected'
  })
  var form = $( 'form' ).on( 'submit', function( e ) {
    e.preventDefault()
    let user_name = $( 'input.username' ).val()
    let user_input = $( 'input.product' ).val()
    socket.emit( 'order', {
      user_name : user_name,
      product : user_input
    })
    $( 'input.product' ).val( '' ).focus()
  })
})