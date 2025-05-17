from fastapi import FastAPI

from app.interface.routers import user


def configure(app: FastAPI):
    app.include_router(user.router, prefix='/api')