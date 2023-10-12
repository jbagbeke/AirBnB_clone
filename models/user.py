#!/usr/bin/python3
""" This is the user module """
from models.base_model import BaseModel


class User(BaseModel):
    """ This is the User class """
    email = ""
    password = ""
    firstname = ""
    last_name = ""
