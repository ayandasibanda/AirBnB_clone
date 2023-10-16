#!/usr/bin/python3
'''Module to create a unique FileStorage instance for the application'''

from models.engine.file_storage import FileStorage

'''A variable storage, an instance of FileStorage'''
storage = FileStorage()
storage.reload()
