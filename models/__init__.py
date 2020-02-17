#!/usr/bin/python3
from models import base_model
from models import user
from models import state
from models import city
from models import amenity
from models import place
from models import review
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
