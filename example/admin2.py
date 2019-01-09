import socketio

sio = socketio.Client()


@sio.on("connect")
def connect():
    print("Connected to server")
    sio.emit("subscribe", {"room": "room": "testing:testing"})


@sio.on("coordinates")
def coordinates(data):
    print("Received coordinates ", data)


sio.connect("https://shuttle-up-tracking.herokuapp.com")  # connect to prod server
# sio.connect("http://localhost:3000")  # connect to server
sio.wait()
