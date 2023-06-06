from fastapi import FastAPI
from application.core.db import database
from application.router import router
app = FastAPI()
app.include_router(router)
sleep_time = 10

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
def root():
    return {
        "message": "/"
    }