from flask import session, request, render_template, Flask
from flask_socketio import SocketIO, emit, join_room, leave_room
io = SocketIO()
app = Flask(__name__)
io.init_app(app)

io.on('connect')
def con(msg):
    emit("welcome", {"data": "Welcome"})


if __name__ == '__main__':
    io.run(app, debug=True, port=5000)