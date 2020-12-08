var socket = io();
socket.on('connect', function() {
	socket.emit('my event', {data: 'I\'m connected!'});
});

$('#message').focus();

$('form').on('submit', function(event){
	event.preventDefault();
	let username = $('#username').val();
	let message = $('#message').val();

	socket.emit(
		'chat event',
		{
			username: username,
			message: message
		})
})

socket.on('chat response', function(data) {
	console.log(data);
	$('.message_box').append(`<div><b><span class='recipient'>${data.username}:</span></b><span class='chatMessage'>${data.message}</span><div>`);
})
