# In the name of GOD

from fastapi import FastAPI, Depends, Request
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager


from api.v1 import notify_api
from db.db import collections, databases, sess_db
from config.middlewares import InternalSecurityMiddleware
from config.config import LOGGING_CONFIG



@asynccontextmanager
async def lifespan(app: FastAPI):
    notification_db = await sess_db()
    collections["notification_collection"] = notification_db.database["notification_collection"]
    yield
    collections.clear()
    notification_db.client.close()

app = FastAPI(lifespan=lifespan)
app.include_router(notify_api.router)
app.add_middleware(InternalSecurityMiddleware)


@app.get("/")
def root():
    return JSONResponse({"message": "Hello..."}, status_code=200)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8005, log_level="debug", reload=True)