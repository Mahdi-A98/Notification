# In the name of GOD

import httpx
import json

from config import settings
from utils.secure_communicate import Encryption

class AccountService:
    code_keys = {"acc_ntf_key1":settings.ACC_NTF_KEY1,
                "acc_ntf_key2":settings.ACC_NTF_KEY2,
                "acc_ntf_key3": settings.ACC_NTF_KEY3}

    Encrypt_tools = Encryption(settings.NTF_ACC_SHARED_KEY, code_keys)

    @classmethod
    async def register_user(cls, data):
        url = settings.ACCOUNT_SERVICE_URL + '/users/register'
        response = await cls.encrypt_and_send(data, url)
        return response        

    @classmethod
    async def login_user(cls, data):
        url = settings.ACCOUNT_SERVICE_URL + '/users/login'
        response = await cls.encrypt_and_send(data, url)
        return response        

    @classmethod
    async def encrypt_and_send(cls, data, url, headers={}):
        encrypted_data = cls.Encrypt_tools.encrypt_data(data)
        async with httpx.AsyncClient() as client:
            headers.update({"internal-service":"notification"})
            response = await client.post(url=url, data=json.dumps(encrypted_data), headers=headers)
        response._content = json.loads(cls.Encrypt_tools.decrypt_data(response.content))
        return response        

