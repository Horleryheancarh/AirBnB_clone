#!/usrbin/python3
"""
City Model
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Defines city to look for
    """
    state_id = ''
    name = ''
