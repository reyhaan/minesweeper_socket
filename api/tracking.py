import socketio
import os

from typing import Dict

redis_mgr = socketio.RedisManager(
    "redis://h:pc34db66b4af76a09bb1f3698a2ff340a76ed4f9ffdd7800f621c66780f8f9a34@ec2-3-81-188-41.compute-1.amazonaws.com:24679"
    if os.getenv("ENV") is not "dev"
    else os.getenv("REDIS_DEV")
)
sio = socketio.AsyncServer(async_mode="aiohttp")


@sio.on("subscribe")
def subscribe(sid: str, data: Dict[str, str]):
    sio.enter_room(sid, data["room"])


@sio.on("coordinates")
async def coordinates(sid, data: Dict[str, str]):
    await sio.emit(event="coordinates", data=data, room=data["room"])

