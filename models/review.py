#!/usrbin/python3
"""
Review Model
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Reviews by users
    """
    place_id = ''
    user_id = ''
    text = ''
