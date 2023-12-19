@asynccontextmanager
async def lifespan(app: FastAPI):
    notification_db = await sess_db()
    collections["notification_collection"] = notification_db.database["notification_collection"]
    yield
    collections.clear()
    notification_db.client.close()
