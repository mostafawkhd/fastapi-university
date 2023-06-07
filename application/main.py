from fastapi import FastAPI
from application.core.db import database
from application.router import router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.include_router(router)
sleep_time = 10
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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