#!/usrbin/python3
"""
User Model
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines Users model
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
