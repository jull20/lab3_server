from fastapi import FastAPI
from v1 import authRouter, productsRouter, reportRouter, userRouter

def set_routers(app: FastAPI):
    app.include_router(authRouter)
    app.include_router(productsRouter)
    app.include_router(reportRouter)
    app.include_router(userRouter)


def use_session(app: FastAPI):
    pass