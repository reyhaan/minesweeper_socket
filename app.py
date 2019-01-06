import os
import socketio

from dotenv import load_dotenv
from sanic import Sanic
from sanic.request import Request
from sanic.log import logger
from sanic.response import json

load_dotenv()

app: Sanic = Sanic()
redis_mgr = socketio.RedisManager(os.getenv('REDIS') if os.getenv('ENV') is not 'dev' else os.getenv('REDIS_DEV'))
sio = socketio.AsyncServer(async_mode='sanic')

@app.route('/ping')
async def ping(request: Request):
  return json({'ping': 'pong'})

@sio.on('connect')
def connect(sid, environ):
    logger.info(f'client connected - {sid}')

if __name__ == '__main__':
  sio.attach(app)
  app.run(host='0.0.0.0', port=os.getenv('PORT'), debug=True if os.getenv('ENV') is not 'dev' else False)