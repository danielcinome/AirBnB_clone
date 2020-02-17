#!/usr/bin/python3
from models import base_model
from models import user
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
