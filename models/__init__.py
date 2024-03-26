#!/usr/bin/python3
"""
Module: __init__.py

This module initializes the models package.
"""

from models.engine import file_storage

# Initialize the file storage engine
storage = file_storage.FileStorage()

# Load data from storage
storage.reload()

