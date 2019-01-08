import socketio

sio = socketio.Client()


@sio.on("connect")
def connect():
    print("Connected to server")
    print("Sending coordinates")
    for _ in range(100):
        sio.emit(
            "coordinates", {"lat": 20.222, "lon": 34.444, "room": "testing:testing"}
        )


sio.connect("http://localhost:3000")  # connect to server
sio.disconnect()
