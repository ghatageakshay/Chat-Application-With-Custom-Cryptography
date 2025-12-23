🔐 Secure Chat Application with Custom Two-Layer Cryptography
📌 Project Overview

This project is a real-time secure chat application developed using Flask, Flask-SocketIO, HTML, CSS, and JavaScript.
The main goal of this project is to demonstrate how secure communication can be achieved using a custom two-layer encryption technique while enabling real-time messaging between users.

Users can chat in real time through a web interface, while all messages are encrypted and decrypted internally, ensuring privacy and data security.

🚀 Features

Real-time chat using WebSockets (Flask-SocketIO)

Custom two-layer encryption:

Emoji-based cipher

Binary encoding

Secure message transmission

Clean and responsive UI

Backend encryption and decryption using Python

Frontend built using HTML, CSS, and JavaScript

🔐 Encryption Technique (Two-Layer Cryptography)
🔹 Layer 1: Emoji Cipher

Each character (A–Z, numbers, symbols) is converted into a unique emoji.

This acts as a substitution cipher.

🔹 Layer 2: Binary Encoding

Each emoji is further converted into a binary representation.

This adds an additional layer of security.

🔄 Decryption

Binary → Emoji

Emoji → Original text

This makes the communication difficult to understand even if intercepted.

⚙️ Tech Stack
Frontend

HTML

CSS

JavaScript

Socket.IO (Client)

Backend

Python

Flask

Flask-SocketIO

📂 Project Structure
chatApp/
│
├── app.py              # Flask backend + SocketIO
├── ciphear.py          # Custom encryption & decryption logic
├── templates/
│   └── index.html      # Frontend UI
└── README.md

🔄 How Real-Time Chat Works

User opens the chat application in the browser.

User types a message.

Message is encrypted using custom cryptography.

Encrypted message is sent to the Flask server via WebSocket.

Server broadcasts the encrypted message to connected clients.

Message is decrypted and displayed in readable format on the UI.

▶️ How to Run the Project
1️⃣ Install Required Packages
pip install flask flask-socketio

2️⃣ Run the Server
python app.py

3️⃣ Open in Browser
http://127.0.0.1:5000


Open the same URL in two browser tabs to test real-time chat.

🧪 Example

Input Message:

Hello


Encrypted Form (Internal):

Emoji → Binary


Displayed to User:

Hello


Encryption and decryption remain hidden from the user.

🎯 Applications

Secure messaging systems

Educational demonstration of cryptography

Real-time communication platforms

Cybersecurity projects

🔮 Future Enhancements

User authentication

Chat rooms

End-to-end encryption keys

Message history storage

Deployment on cloud platforms

👨‍💻 Developed By

Akshay Ghatage
Project – Secure Chat Application
