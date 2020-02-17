#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """
        Class User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
