#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    intro = ""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        "Quit command to exit the program"
        return True;

    def do_EOF(self, arg):
        "Quit command to exit the program\n"
        return True;

    def emptyline(self):
        return;

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
        if (len(arg) == 0):
            print("** class name missing **")
        else:
            try:
                command = arg.split(" ")
                new = globals()[command[0]]()
                if (len(command) == 1):
                    print("** instance id missing **")
                    return
                obj = storage.all()
                for key, value in obj.items():
                    if (value.id == command[1]):
                        print(value)
                        return
                print("** no instance found **")
            except KeyError:
                print("** class doesn't exist **")
                



if __name__ == '__main__':
    HBNBCommand().cmdloop()
