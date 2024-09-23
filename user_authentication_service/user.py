#!/usr/bin/env python3
"""
user model creating a SQLAlchemy model named User for database table
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Base class for declarative base
Base = declarative_base()


class User(Base):
    """
    User class model for users table
    """

    # Table name
    __tablename__ = 'users'

    # Columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False, unique=True)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=False)
