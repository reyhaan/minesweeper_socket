import os
import socketio
from aiohttp.web import Application, RouteTableDef, json_response, Request, run_app

from api.tracking import sio
from dotenv import load_dotenv

load_dotenv()

app: Application = Application()
routes: RouteTableDef = RouteTableDef()

@routes.get('/ping')
async def ping(request: Request):
  return json_response({'ping': 'pong'})

if __name__ == '__main__':
  app.add_routes(routes)
  sio.attach(app)
  run_app(app, port=os.getenv('PORT', 3000))
  