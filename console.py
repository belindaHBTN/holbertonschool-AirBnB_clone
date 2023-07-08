#!/usr/bin/python3

"""A program that contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the command interpreter"""
    class_name_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }
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
        elif args not in HBNBCommand.class_name_dict.keys():
            print("** class doesn't exist **")
        else:
            my_model = HBNBCommand.class_name_dict[args]()
            my_model.save()
            print(my_model.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the class
        name and id"""
        arg_list = args.split()

        if not args:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.class_name_dict.keys():
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

    def do_destroy(self, args):
        """Destroys an object instance based on class name and id"""
        arg_list = args.split()

        if not args:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.class_name_dict.keys():
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            key_str = arg_list[0] + "." + arg_list[1]
            for key, value in obj_dict.items():
                if key == key_str:
                    del obj_dict[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, args):
        """Print string representation of instances based on class name"""
        list_of_ins_str = []
        list_of_ins_obj = []
        obj_dict = storage.all()
        for value in obj_dict.values():
            list_of_ins_str.append(value.__str__())
            list_of_ins_obj.append(value)

        if not args:
            print(list_of_ins_str)
        elif args in HBNBCommand.class_name_dict.keys():
            filtered_list = []
            for obj in list_of_ins_obj:
                if obj.__class__.__name__ == args:
                    filtered_list.append(obj.__str__())
            print(filtered_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance by adding or updating attribute"""
        arg_list = args.split()

        if not args:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.class_name_dict.keys():
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif len(arg_list) == 2:
            print("** attribute name missing **")
        elif len(arg_list) == 3:
            print("** value missing **")
        else:
            arg_list[3] = arg_list[3].replace('"', '')
            obj_dict = storage.all()
            key_str = arg_list[0] + "." + arg_list[1]
            for key, value in obj_dict.items():
                if key == key_str:
                    setattr(value, arg_list[2], arg_list[3])
                    storage.save()
                    return
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
