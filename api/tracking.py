import socketio
import os

from typing import Dict

sio = socketio.AsyncServer(async_mode="aiohttp")

@sio.on("subscribe")
async def subscribe(sid: str, data: Dict[str, str]):
    sio.enter_room(sid, data["room"])

@sio.on("coordinates")
async def coordinates(_, data: Dict[str, str]):
    await sio.emit(event="coordinates", data=data, room=data["room"])
