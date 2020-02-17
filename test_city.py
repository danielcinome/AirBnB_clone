#!/usr/bin/python3
from models import *
from models.state import State
from models.city import City
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)
print("-- Create a new User --")
my_user = User()
my_user.first_name = 'Giovanni'
my_user.last_name = 'Perez'
my_user.email = 'pepito1@giovani.com'
print(my_user)
print("-----------------------")

print("-- Create a new State --")
my_state = State()
my_state.name = "Antioquia"
print(my_state)
print("-----------------------")

print("-- Crate a  new City --")
my_city = City()
my_city.name = "Medellin"
my_city.state_id = my_state.id
print(my_city)
print("-----------------------")

print("-- Crate a  new Amenity --")
my_amenity = Amenity()
my_amenity.name = "Wi-Fi"
print(my_amenity)
print("-----------------------")

print("-- Crate a  new Place --")
my_place = Place()
my_place.city_id = my_city.id
my_place.user_id = my_user.id
my_place.name = 'Bahamas'
my_place.description = 'Las Bahamas es un lugar muy Cool'
my_place.number_rooms = 4
my_place.number_bathrooms = 2
my_place.max_guest = 4
my_place.price_by_night = 200
my_place.lalitude = 25.0342808
my_place.longitude = -77.3962784
my_place.amenity_ids = str(my_amenity.id)
print(my_place)
print("-----------------------")

print("-- Crate a  new Review --")
my_review = Review()
my_review.place_id = my_place.id
my_review.user_id = my_user.id
my_review.text = 'Asombroso'
print(my_review)
print("-----------------------")
