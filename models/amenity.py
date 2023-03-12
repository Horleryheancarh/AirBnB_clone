#!/usrbin/python3
"""
Amenities Model
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Defines amenities that user can choose from
    """
    name = ''
