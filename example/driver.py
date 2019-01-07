import socketio

sio = socketio.Client()

@sio.on('connect')
def connect():
  print('Connected to server')
  print('Sending coordinates')
  for i in range(100):
    sio.emit('coordinates', {'lat': 'teating', 'lon': 'testing', 'room': 'testing:testing'})

sio.connect('http://localhost:3000') # connect to server
sio.disconnect()