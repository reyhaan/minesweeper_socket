import socketio
import os

from typing import Dict

redis_mgr = socketio.RedisManager(os.getenv('REDIS_URL') if os.getenv('ENV') is not 'dev' else os.getenv('REDIS_DEV'))
sio = socketio.AsyncServer(async_mode='aiohttp')

@sio.on('subscribe')
def subscribe(sid: str, data: Dict[str, str]):
    sio.enter_room(sid, data['room'])

@sio.on('coordinates')
async def coordinates(sid, data: Dict[str, str]):
  await sio.emit(event='coordinates', data=data, room=data['room'])