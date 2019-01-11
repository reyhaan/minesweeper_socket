import os
import socketio
import dotenv
from aiohttp import web
from api.tracking import sio

async def init():
    app: web.Application = web.Application()
    routes: web.RouteTableDef = web.RouteTableDef()

    @routes.get("/")
    async def ping(request: web.Request):
        return web.json_response({"Shuttle-up": "Event Service"})

    sio.attach(app)
    app.add_routes(routes)
    return app

if __name__ == "__main__":
    dotenv.load_dotenv()
    redis_url = os.getenv("REDIS_DEV") if os.getenv("ENV") == "dev" else os.getenv("REDIS_URL")
    REDIS_MGR = socketio.AsyncRedisManager(redis_url)
    app = init()
    web.run_app(app, port=os.getenv("PORT", 3000))
