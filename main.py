from flask import render_template
from flask_socketio import SocketIO, emit, join_room, leave_room
from app import create_app
from app.models import db, Room


app = create_app()


@app.route('/')
def main():
    return render_template('index.html')


socketio = SocketIO(app, logger=True, engineio_logger=True)

@socketio.on('disconnect')
def disconnect():
    print('Usuario desconectado')


@socketio.on('join_room')
def on_join_room(data):
    code = data['code']
    # roomData: Room = Room.query.filter_by(code=code).first()
    join_room(code)
    emit('join_room_success', {'code': code})

@socketio.on('send_message')
def on_send_message(data):
    code = data['code']
    message = data['message']
    emit('new_message', {'message': message}, include_self=False, to=code)


if __name__ == '__main__':
    socketio.run(app)
