#!/usr/bin/python3
"""Initialize a unique FileStorage instance for the application.

This module creates an instance of the FileStorage class, which is responsible
for handling the serialization and deserialization of objects to and from JSON files.

Attributes:
    storage (FileStorage): An instance of the FileStorage class.
"""
from models.engine.file_storage import FileStorage

# Initialize a unique FileStorage instance
storage = FileStorage()
# Load existing data from the storage file
storage.reload()
