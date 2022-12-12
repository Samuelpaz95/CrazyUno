from flask import render_template
from flask_socketio import SocketIO
from app import create_app


app = create_app()

@app.route('/')
def main():
    return render_template('index.html')


socketio = SocketIO(app, logger=True, engineio_logger=True)

if __name__ == '__main__':
    socketio.run(app)
