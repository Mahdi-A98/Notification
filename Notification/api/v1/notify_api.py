# In the name of GOD

from fastapi import APIRouter, Depends, status, Body
from fastapi.responses import Response, JSONResponse

from typing import Annotated
import json

from models.notification import EmailNotification
from config.dependencies import AllowedServices, get_service
from db.db import databases, collections
from utils.email_tools import send_email


ServiceDep = Annotated[str, Depends(get_service)]



router = APIRouter(
    prefix="/notification",
    tags=["notification"],
    responses={404: {"description":"Not found"}, 307: {"detail":"method not allowed"}},
    dependencies=[Depends(get_service)])




@router.post("/send_email_notification", status_code=status.HTTP_201_CREATED,
            dependencies=[Depends(AllowedServices(["authentication", "account"]))])
async def send_email_notification(email_notification: EmailNotification= Body(...)):

    notification_collection = collections["notification_collection"]
    send_email(email_notification.reciever_email, email_notification.subject, email_notification.message)
    result = notification_collection.insert_one(email_notification.dict())
    # TODO add attachment from request files to email
    return JSONResponse(str(result), status_code=status.HTTP_200_OK)
