from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({"hello": "world"})


app = Starlette(
    debug=True,
    routes=[
        Route("/", homepage),
    ],
)


async def ping(request):
    return JSONResponse("pong")


app = Starlette(
    debug=True,
    routes=[
        Route("/ping", ping),
    ],
)
