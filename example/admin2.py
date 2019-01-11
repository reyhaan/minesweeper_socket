import socketio

sio = socketio.Client()


@sio.on("connect")
def connect():
    print("Connected to server")
    sio.emit("subscribe", {"room": "testing:2"})

@sio.on("coordinates")
def coordinates(data):
    print("Received coordinates ", data)

sio.connect("http://localhost:3000")  # connect to server
sio.wait()
