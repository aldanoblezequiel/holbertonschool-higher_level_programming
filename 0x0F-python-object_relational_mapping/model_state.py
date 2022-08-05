#!/usr/bin/python3
"""Module State"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """State class initialization"""
    __tablename__ = 'states'
    id = Column(Integer(), primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
