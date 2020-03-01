#!/usr/bin/python3
"""
command interpreter
"""
import re
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
    """
    command interpreter
    """
    intro = ""
    prompt = "(hbnb) "

    @staticmethod
    def comprobation(arg, val_flag):
        """
        Comprobation of conditions needed
        for command destroy and show
        """
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
        """
        Command exit the program
        """
        "Quit command to exit the program"
        return True

    def do_EOF(self, arg):
        """
        Command to exit the program
        """
        "Quit command to exit the program\n"
        return True

    def emptyline(self):
        """
        New line if it's empty line
        """
        return

    def do_create(self, arg):
        """
        Create new instance of one name class
        """
        "Create new instance of one name class"
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
        """
        Print string representation of instance
        """
        "Print string representation of instance"
        HBNBCommand.comprobation(arg, 1)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        "Deletes an instance based on the class name and id"
        HBNBCommand.comprobation(arg, 2)

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        """
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
        """
        instance based on the class name and id
        """
        "instance based on the class name and id"
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
        """
        Check is parameter of updtade is a string
        """
        count = 0
        for i in str:
            if (i.isalpha()):
                count = count + 1
            if (count >= 2):
                return True
        return False

    def default(self, line):
        """
        Call on an input line when the command prefix is not recognized
        """
        try:
            type_class = line.split('.')
            if (type_class[1] == 'all()'):
                HBNBCommand.do_all(all, type_class[0])
            elif (type_class[1] == 'count()'):
                count = 0
                obj = storage.all()
                for key in obj:
                    if (key.split(".")[0] == type_class[0]):
                        count = count + 1
                print(count)
            elif (type_class[1][:4] == 'show'):
                token_show = type_class[0] + ' ' + type_class[1][6:-2]
                HBNBCommand.do_show(self, token_show)
            elif (type_class[1][:7] == 'destroy'):
                s = type_class[1]
                st = type_class[0] + " " + s[s.find("(") + 2:s.find(")") - 1]
                HBNBCommand.do_destroy(self, st)
            elif (type_class[1][:6] == 'update'and
                    type_class[1].count("{") == 1):
                split = line.split(",", 1)
                getId = type_class[1].split(",")
                getId = getId[0][getId[0].find("(") + 2:getId[0].find(")")]
                dit = eval(split[1][:-1])
                getId = str(type_class[0]) + " " + str(getId)
                for key, value in dit.items():
                    setC = getId + " " + key + " " + str(value)
                    print(setC)
                    HBNBCommand.do_update(self, setC)
            elif (type_class[1][:6] == 'update'):
                token = type_class[1]
                token_update = token[token.find("(") + 1:token[1].find(")")]
                token_update = re.sub(',|"', '', token_update)
                token_update = type_class[0] + ' ' + token_update
                HBNBCommand.do_update(self, token_update)
        except Exception:
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
