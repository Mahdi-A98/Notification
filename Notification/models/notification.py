
from typing import Optional, List

from pydantic import ConfigDict, BaseModel, Field, EmailStr, StringConstraints
from pydantic.functional_validators import BeforeValidator
from pydantic.types import SecretStr, constr

from typing_extensions import Annotated

from bson import ObjectId
from pymongo import ReturnDocument
from datetime import datetime



# Represents an ObjectId field in the database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]

class EmailNotification(BaseModel):
    created_at : datetime = Field(default_factory=datetime.now)
    reciever_username : Optional[str] = None
    reciever_email : EmailStr
    subject: Optional[str] = None
    message: Optional[str] = None
    service: Optional[str] = None