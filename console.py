#!/usr/bin/python3
import cmd
import shlex
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    intro = ""
    prompt = "(hbnb) "

    @staticmethod
    def comprobation(arg, val_flag):
        if (len(arg) == 0):
            print("** class name missing **")
        else:
            try:
                command = arg.split(" ")
                globals()[command[0]]
                if (len(command) == 1):
                    print("** instance id missing **")
                    return
                obj = storage.all()
                for key, value in obj.items():
                    nameSplit = key.split(".")[0]
                    if (value.id == command[1] and command[0] == nameSplit):
                        if (val_flag == 1):
                            print(value)
                        elif (val_flag == 2):
                            del obj[key]
                            storage.save()
                        return
                print("** no instance found **")
                return
            except KeyError:
                print("** class doesn't exist **")

    def do_quit(self, arg):
        "Quit command to exit the program"
        return True

    def do_EOF(self, arg):
        "Quit command to exit the program\n"
        return True

    def emptyline(self):
        return

    def do_create(self, arg):
        "Create new instance of name class"
        if (len(arg) == 0):
            print("** class name missing **")
        else:
            try:
                new = globals()[arg]()
                print(new.id)
                new.save()
            except KeyError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        "Print string representation of instance"
        HBNBCommand.comprobation(arg, 1)

    def do_destroy(self, arg):
        "Deletes an instance based on the class name and id"
        HBNBCommand.comprobation(arg, 2)

    def do_all(self, arg):
        "Prints all string representation of all instances"
        obj = storage.all()
        flag = 0
        val = []
        if (len(arg) > 0):
            flag = 1
            if arg not in globals():
                print("** class doesn't exist **")
                return
        for key, value in obj.items():
            name_key = key.split(".")
            if (flag == 1):
                if (name_key[0] == arg and flag == 1):
                    val.append(value.__str__())
            else:
                val.append(value.__str__())
        if (len(val) >= 1):
            print(val)

    def do_update(self, arg):
        " instance based on the class name and id"
        if (len(arg) == 0):
            print("** class name missing **")
        else:
            try:
                command = shlex.split(arg)
                print(command)
                globals()[command[0]]
                if (len(command) == 1):
                    print("** instance id missing **")
                    return
                obj = storage.all()
                nameKey = command[0] + '.' + command[1]
                if (nameKey in obj):
                    if (len(command) < 3):
                        print("** attribute name missing **")
                        return
                    elif (len(command) < 4):
                        print("** value missing **")
                        return
                    objtmp = obj[nameKey]
                    dicObjtmp = objtmp.to_dict()
                    if (HBNBCommand.checkString(command[3])):
                        stri = str(command[3])
                    elif ("." in command[3] and command[3].count('.') == 1):
                        command[3] = float(command[3])
                    elif (command[3][0] not in "'" and command[3] not in "."):
                        command[3] = int(command[3])
                    if (command[2] in dicObjtmp):
                        dicTmp = {command[2]: command[3]}
                        dicObjtmp.update(dicTmp)
                    else:
                        dicObjtmp[command[2]] = command[3]

                    print(dicObjtmp)
                    swap = globals()[command[0]](**dicObjtmp)
                    print(swap)
                    del obj[nameKey]
                    swap.save()
                    obj[nameKey] = swap
                    swap.save()
                else:
                    print("** no instance found **")
                    return
            except KeyError:
                print("** class doesn't exist **")


    @staticmethod
    def checkString(str):
        count = 0
        for i in str:
            if (i.isalpha()):
                count = count + 1
            if (count >= 2):
                return True
        return False

    def do_User(self, arg):
        HBNBCommand.type_class('User', arg)
    
    def do_BaseModel(self, arg):
        HBNBCommand.type_class('BaseModel', arg)

    @staticmethod
    def type_class(t_class, arg):
        """
        identify action type <class name>.action_name()
        """
        name_key = arg.split(".")
        if (name_key[1] == 'all()'):
            HBNBCommand.do_all(all, t_class)
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
