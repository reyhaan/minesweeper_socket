# ShuttleUp Tracking

Realtime location tracking for ShuttleUp

### Integration Instructions
#### Socket-io Events
* Subscribe
  * Used to subscribe to room between admin and driver
* Coordinates
  * Client
    * Sends coordinates to server
  * Server
    * forwards coordinates to admin

#### Sample Code
* Admin
```
import socketio

sio = socketio.Client()


@sio.on('connect')
def connect():
  print('Connected to server')
  sio.emit('subscribe', {'room': 'testing'}) # subscribes to a room as connect to server

@sio.on('coordinates')
def coordinates(data):
  print('Received coordinates ', data) # handles coordinates

sio.connect('http://localhost:3000') # connect to server
sio.wait() # waits until connection closes
```
* Driver
```
import socketio

sio = socketio.Client()

@sio.on('connect')
def connect():
  print('Connected to server')
  print('Sending coordinates')
  # simulates sending hundred coordinates into a room
  for i in range(100):
    sio.emit('coordinates', {'lat': 'teating', 'lon': 'testing', 'room': 'testing:testing'})

sio.connect('http://localhost:3000') # connect to server
sio.disconnect() # disconnects connection
```

### Setup Prerequisites
* Python >= 3.7 - [Install](https://www.python.org/downloads/release/python-372/)
* Pip - [Install](https://pip.pypa.io/en/stable/installing/)
* Docker - [Install](https://docs.docker.com/install/)

### Setup Instructions
* Fork the repo
* Clone the repo by running the following command
```shell
git clone https://github.com/tktaofik/shuttle-tracking.git
cd shuttle-tracking
```
* Change git remote origin to your fork and upstream to this repo
```shell
git remote set-url origin https://github.com/USERNAME/shuttle-tracking.git
git remote add upstream https://github.com/tktaofik/shuttle-tracking.git
```
> replace USERNAME with your github username
* Create virtual environment and activate
```shell
python3 -m venv venv
source ./venv/bin/activate
```
* Install dependencies
```shell

make init
```

If you've made it here, you're all set!

### Running the application 
* It as simple as running the following command
```
make dev
```

### Production Deployment
* Make sure to have redis server running
* Set redis url environment variable REDIS
