import socketio

sio = socketio.Client()


@sio.on("connect")
def connect():
    print("Connected to server")
    print("Sending coordinates")
    for i in range(100):
        sio.emit("coordinates", {"lat": 230, "lon": 444, "room": "driver:1234"})


# sio.connect('http://localhost:3000') # connect to server
sio.connect("https://shuttle-up-tracking.herokuapp.com")  # connect to server
sio.disconnect()
