#!/usr/bin/python3

"""A program that contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


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

    def do_create(self, args):
        """Creates a new instance, saves it and prints the id"""
        if not args:
            print("** class name missing **")
        elif args != "BaseModel":
            print("** class doesn't exist **")
        else:
            my_model = BaseModel()
            my_model.save()
            print(my_model.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the class
        name and id"""
        arg_list = args.split()

        if not args:
            print("** class name missing **")
        elif arg_list[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            key_str = arg_list[0] + "." + arg_list[1]
            for key, value in obj_dict.items():
                if key == key_str:
                    print(value)
                    return
            print("** no instance found **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
