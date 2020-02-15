#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    intro = ""
    prompt = "(hbnb) "

    def do_quit(self, args):
        "Quit command to exit the program"
        return True;

    def do_EOF(self, args):
        "Quit command to exit the program"
        return True;

    def emptyline(self):
        return;


if __name__ == '__main__':
    HBNBCommand().cmdloop()
