import socketio
import time

sio = socketio.Client()

@sio.on("connect")
def connect():
    print("Connected to server")
    for i in range(1,3):
        for _ in range(20):
            print(f"Sending coordinates to admin {str(i)}")    
            sio.emit(
                "coordinates", {"lat": 20.222, "lon": 34.444, "room": f"testing:{str(i)}"}
            )
            time.sleep(0.5)
    
sio.connect("http://localhost:3000")  # connect to server
sio.disconnect()
