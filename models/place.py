#!/usrbin/python3
"""
Place Model
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Defines place
    """
    city_id = ''
    user_id = ''
    description = ''
    number_bathrooms = 0
    number_rooms = 0
    price_by_night = 0
    max_guest = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    name = ''
