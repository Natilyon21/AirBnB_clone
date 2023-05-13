#!/usr/bin/python
""" 
contains the class State
"""
from models.base_model import BaseModel


class State(BaseModel):
    """the features of state """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
