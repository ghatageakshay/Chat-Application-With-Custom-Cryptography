from flask import Flask, render_template
from flask_socketio import SocketIO, send
from ciphear import encrypt_msg, encrypt_to_binary, decrypt_from_binary, decrypt_msg

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(payload):
    """
    Expect payload from client in the format:
    {
        "text": "<plaintext message>",
        "clientId": "<sender identifier>"
    }
    """
    text = payload.get('text') if isinstance(payload, dict) else str(payload)
    client_id = payload.get('clientId') if isinstance(payload, dict) else None

    print("Received:", text)

    # Encrypt message
    emoji_layer = encrypt_msg(text)
    binary_layer = encrypt_to_binary(emoji_layer)
    
    # Broadcast: keep encrypted payload on the server, share plaintext with clients
    socketio.emit('receive_message', {
        'plaintext': text,
        'encrypted': binary_layer,
        'clientId': client_id
    })

if __name__ == '__main__':
    socketio.run(app, debug=True)
