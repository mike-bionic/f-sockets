import os
from flask import Flask, render_template, request, session, url_for
from flask_socketio import SocketIO
from flask_socketio import emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fij043mf3iprnfvu5tn3'
socketio = SocketIO(app)

@app.route('/')
def index():
	return render_template('chat/main.html')


@socketio.on('order')
def on_order(json, methods=['GET', 'POST']):
	print("received order " + str(json))
	socketio.emit('server-message', json, callback=messageReceived)


@socketio.on('connect')
def on_connect():
	if not authenticate_user():
		return False
	emit('message', user + ' has joined.', broadcast=True)


@socketio.on('post-message')
def on_post_message(message):
	emit('message', message, broadcast=True)


@socketio.on('disconnect')
def on_disconnect():
	emit('message', user +' has left.', broadcast=True)

if __name__ == '__main__':
	socketio.run(app, debug=True)