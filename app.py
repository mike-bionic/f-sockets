from flask import Flask, render_template
from flask_socketio import SocketIO, emit, Namespace

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def main():
	return render_template('main.html')


@socketio.on('connect')
def handle_connect():
	print('client connected')
	emit('chat response', {'username':'server','message': 'successfully connected'}, broadcast=True)


@socketio.on('disconnect')
def handle_disconnect():
	print('client disconnected')
	emit('chat response', {'username':'server','message': 'disconnected'}, broadcast=True)


@socketio.on('message')
def handle_message(message):
	print(f'Received message {message}')


@socketio.on('json')
def handle_json(json):
	print(f'Received json {str(json)}')


@socketio.on('my event')
def handle_my_event(json):
	print(f'Received event {str(json)}')

def store_message(message_data):
	# print(message_data)
	username = message_data['username']
	message = message_data['message']
	print(f'Storing the message "{message}" of user "{username}"')


@socketio.on('chat event')
def handle_chat_event(json):
	emit('chat response', json, callback=store_message(json), broadcast=True)


@socketio.on_error()
def error_handler(e):
	print("error occured (root namespace)")
	print(e)

@socketio.on_error_default
def default_error_handler(e):
	print("error occured (default)")
	print(e)


class ChatNamespace(Namespace):
	def on_connect(self):
		print("connected to a class Namespace")

	def on_disconnect(self):
		print("disconnected from class Namespace")

	def on_my_event(self, data):
		emit('my_response', data)

socketio.on_namespace(ChatNamespace('/chat'))


if __name__ == '__main__':
	app.run(host='0.0.0.0')
	socketio.run(app)