from fastapi import FastAPI
from v1 import mainRouter

def set_routers(app: FastAPI):
    app.include_router(mainRouter)


def use_session(app: FastAPI):
    pass