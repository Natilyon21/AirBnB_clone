#!/usr/bin/python3
"""initializes the packages"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
