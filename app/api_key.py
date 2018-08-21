from app.db import api_keys
import os
from uuid import uuid4
import bcrypt
import hashlib

SALT = bytes(os.getenv('SALT').encode('utf8'))


def api_key_exists(api_key):
    hashed_api_key = bcrypt.hashpw(
        api_key.encode('utf8'),
        SALT
    )

    current_api_key = api_keys.find_one({'hashed_api_key': hashed_api_key})

    print(current_api_key)
    if current_api_key is not None:
        return True
    return False


def create_api_key():
    new_api_key = str(uuid4())
    hashed_api_key = bcrypt.hashpw(
        new_api_key.encode('utf8'),
        SALT
    )
    api_keys.insert({'hashed_api_key': hashed_api_key})
    print("Your new API key is : {}, don't lose it!".format(new_api_key))
    return new_api_key
