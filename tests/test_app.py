import os 
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
import app
import dotenv
import json
import socketio
from aiohttp import ClientSession
from expects import expect, be, have_keys, have_key

@pytest.fixture
async def server(aiohttp_client):
    dotenv.load_dotenv()
    server = await app.init()
    return await aiohttp_client(server)

async def test_tracking_status(server):
    response = await server.get('/')
    expect(response.status).to(be(200))
    expect(await response.json()).to(have_key('Shuttle-up'))

def test_tracking_service(server):
    admin = socketio.Client()
    driver = socketio.Client()

    coordinates = {"lat": 20.222, "lon": 34.444, "room": "testing"}

    def admin_connect():
        admin.emit("subscribe", {"room": "testing"})

    def admin_coordinates(data):
        expect(data).to(have_keys("lat", "lon", "room"))        

    def driver_connect():
        driver.emit("coordinates", coordinates)

    admin.on("connect", admin_connect)
    admin.on("coordinates", admin_coordinates)
    driver.on("connect", driver_connect)
    
    admin.connect(f"http://{server.host}:{str(server.port)}")
    driver.connect(f"http://{server.host}:{str(server.port)}")
    driver.disconnect()
    admin.disconnect()




