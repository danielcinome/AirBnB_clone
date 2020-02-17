# AirBnB clone - The console

![N|Solid](https://www.holbertonschool.com/holberton-logo.png)
--
![N|Solid](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUZGDONYM4%2F20200217%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200217T153532Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8f648da1018de0fea6a4fc3d3fe548f99f167fce93085e8ad6bda4648aaef20a)
---

## Description

-   data model
-   manage (create, update, destroy, etc) objects via a console / command interpreter
-   store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself)


## Task Project
---
### The console
command interpreter [base_model.py](https://github.com/danielcinome/AirBnB_clone/blob/master/console.py) commands:
-   `quit`  and  `EOF`  to exit the program
-   `help`  (this action is provided by default by  `cmd`  but you should keep it updated and documented)
-   a custom prompt:  `(hbnb)`
-   an empty line +  `ENTER`  shouldn’t execute anything

```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

```

- `create`: Creates a new instance of `Class_name`, saves it (to the JSON file). Ex:
	-  `(hbnb) create BaseModel`

-  `show`: Prints the string representation of an instance based on the class name and `id`. Ex: 
	- `(hbnb) show BaseModel 1234-1234-1234`.

- `destroy`: Deletes an instance based on the class name and `id` (save the change into the JSON file). Ex: 
	- `(hbnb) destroy BaseModel 1234-1234-1234`.

- `all`: Prints all string representation of all instances based or not on the class name. Ex:
	- `(hbnb) all BaseModel` or `$ all`.

- `update`: Updates an instance based on the class name and `id` by adding or updating attribute (save the change into the JSON file). Ex:
	- `(hbnb) update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"`.

---
File Name|Class Name|Task Description
---|---|---
[base_model.py](https://github.com/danielcinome/AirBnB_clone/blob/master/models/base_model.py)|BaseModel| Defines all common attributes/methods for other classes
[file_storage.py](https://github.com/danielcinome/AirBnB_clone/blob/master/models/engine/file_storage.py) | FileStorage |Convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. 
[user.py](https://github.com/danielcinome/AirBnB_clone/blob/master/models/user.py) | User |Class User inherits from the BaseModel class, you instantiates a new user.

-   `email`: string
-   `password`: string
-   `first_name`: string
-   `last_name`: string
---
| | | |
---|---|---
   [state.py](https://github.com/danielcinome/AirBnB_clone/blob/master/models/state.py) | State |Class State inherits from the BaseModel class, you instantiates a new state.
-   `name`: string
----
| | | |
---|---|---
[city.py](https://github.com/danielcinome/AirBnB_clone/blob/master/models/city.py) | City | Class City inherits from the BaseModel class, you instantiates a new city.
-  `state_id`: string : it will be the `State.id`
- `name`: string
---
| | | |
---|---|---
[amenity.py](https://github.com/danielcinome/AirBnB_clone/blob/master/models/amenity.py) | Amenity | Class Amenity inherits from the BaseModel class, you instantiates a new amenity.
- `name`: string
----
| | | |
---|---|---
[place.py](https://github.com/danielcinome/AirBnB_clone/blob/master/models/place.py) | Place | Class Place inherits from the BaseModel class, you instantiates a new place.

-   `city_id`: string : it will be the  `City.id`
-   `user_id`: string : it will be the  `User.id`
-   `name`: string
-   `description`: string
-   `number_rooms`: integer - 0
-   `number_bathrooms`: integer - 0
-   `max_guest`: integer - 0
-   `price_by_night`: integer - 0
-   `latitude`: float - 0.0
-   `longitude`: float - 0.0
-   `amenity_ids`: list of string : it will be the list of  `Amenity.id`  later
---
| | | |
---|---|---
[Review](https://github.com/danielcinome/AirBnB_clone/blob/master/models/review.py) | Review | Class Review inherits from the BaseModel class, you instantiates a new review.
-   `place_id`: string : it will be the  `Place.id`
-   `user_id`: string : it will be the  `User.id`
-   `text`: string


---

## Author

- Daniel Angarita Chinome [@danielchinome](https://twitter.com/danielchinome)

- Giovanni Perez. [@Giovanni_Perez1](https://twitter.com/Giovanni_Perez1)
