#!/usr/bin/env python3
"""
user model creating a SQLAlchemy model named User for database table
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Base class for declarative base
Base = declarative_base()


class User(Base):

    # Table name
    __tablename__ = 'users'

    # Columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)
    session_id = Column(String(255), nullable=True)
    reset_token = Column(String(255), nullable=False)
