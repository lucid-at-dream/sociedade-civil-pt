from flask import Flask, request, render_template, send_from_directory
from flask_socketio import SocketIO, emit
from random import randint
from flask_swagger import swagger
from logging.config import dictConfig
import json
from data import DataLayer

client_path = 'client'

dictConfig({
    'version': 1,
    'root': {
        'level': 'INFO'
    }
})

app = Flask("socivil", template_folder=f"{client_path}/pages")
socketio = SocketIO(app)

connectionString = 'esdb+discover://esdb:2113?tls=false&keepAliveTimeout=10000&keepAliveInterval=10000'
storage = DataLayer(connectionString)
storage.connect()

@app.route('/scripts/<path:path>')
def get_scripts(path):
    return send_from_directory(f'{client_path}/scripts', path)

@app.route('/style/<path:path>')
def get_style(path):
    return send_from_directory(f'{client_path}/style', path)

def validate_shout(shout):
    return len(shout.strip()) > 0

@app.put('/shout')
def put_shout():
    shout = request.form['shout']

    if validate_shout(shout):
        storage.create_shout(shout)
        socketio.emit('shout', [shout])
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
    else:
        return "The shout was deemed invalid", 400

@app.get('/shout')
def get_shouts():
    return storage.list_shouts(100)

@app.route('/swagger')
def get_swagger():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Sociedade Civil PT"
    return swag

@app.route('/docs')
def docs():
    return render_template('swagger.html', app_url=request.url_root)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", debug=True, allow_unsafe_werkzeug=True)
