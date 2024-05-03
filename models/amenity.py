#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import String
from sqlalchemy import Column


class Amenity(BaseModel, Base):
    """Represents an Amenity for a MySQL database."""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity", viewonly=False)
