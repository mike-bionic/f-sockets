from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def main():
	return render_template('main.html')

@socketio.on('message')
def handle_message(message):
	print(f'Received message {message}')


@socketio.on('json')
def handle_json(json):
	print(f'Received json {str(json)}')


@socketio.on('my event')
def handle_my_event(json):
	print(f'Received event {str(json)}')


@socketio.on('chat event')
def handle_chat_event(json):
	emit('chat response', json)

if __name__ == '__main__':
	socketio.run(app)