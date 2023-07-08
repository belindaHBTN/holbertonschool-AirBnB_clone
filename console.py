#!/usr/bin/python3

"""A program that contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the command interpreter"""
    prompt = "(hbnb)"

    def do_quit(self, args):
        """Quit command to exit the program
        """
        raise SystemExit

    def do_EOF(self, args):
        """Quit command to exit the program
        """
        raise SystemExit

    def emptyline(self):
        """Called when the user enters and empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
