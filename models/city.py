#!/usr/bin/python3
""" Class for City"""
from models.base_model import BaseModel

class City(BaseModel):
    """Represents city Class"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)

