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
from expects import expect, equal, have_keys, have_key

@pytest.fixture
async def server(aiohttp_client):
    dotenv.load_dotenv()
    server = await app.init()
    return await aiohttp_client(server)

async def test_tracking_start(server):
    response = await server.get('/')
    expect(response.status).to(equal(200))
    data = await response.json()
    expect(data).to(have_key("Shuttle-up"))
    expect(data["Shuttle-up"]).to(equal("Event Service"))
