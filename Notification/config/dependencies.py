# In the name of GOD
from fastapi import Header, HTTPException, Request
from typing import Annotated, List

from services import SERVICE_CLASSES


async def get_service(request: Request):
    if not request.headers.get("internal-service"):
        raise HTTPException(detail="Access denied.", status_code=403)
    return True


class AllowedServices:
    def __init__(self, allowed_services:List):
        self.allowed_services = allowed_services

    async def __call__(self, request:Request):
        if not request.headers.get("internal-service"):
            raise HTTPException(detail="Access denied.", status_code=403)
        if not request.headers.get("internal-service") in self.allowed_services:
            raise HTTPException(detail=f"This endpoint is restricted to {' ,'.join(self.allowed_services)} services.", status_code=403)
        return True