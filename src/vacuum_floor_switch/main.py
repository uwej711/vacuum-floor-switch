from fastapi import FastAPI

from .api import switch_floor_router
from .web import web_router

app = FastAPI()
app.include_router(switch_floor_router)
app.include_router(web_router)
