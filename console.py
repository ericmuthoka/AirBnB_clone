#!/usr/bin/python3
"""
This is the entry point of the command interpreter.
"""

import cmd
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """Custom command interpreter."""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit the program."""
        return True

    def do_EOF(self, line):
        """Exit the program on Ctrl+D."""
        return True

    def help_help(self):
        """Help for the help command."""
        print("The help command displays a list of all the available commands.")

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_create(self, line):
        """Create a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        Usage: create <class name>
        """
        if not line:
            print("** class name missing **")
        elif line not in ["BaseModel", "State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{line}()")
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            all_objects = storage.all()
            if key in all_objects:
                print(all_objects[key])
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances based
        or not on the class name.
        Usage: all [class name]
        """
        args = line.split()
        all_objects = storage.all()
        objects_to_print = []

        if not args:
            for obj in all_objects.values():
                objects_to_print.append(str(obj))
        elif args[0] not in ["BaseModel", "State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        else:
            class_name = args[0]
            if class_name == "User":
                class_name = "users"  # Convert to the attribute name in storage
            for key in all_objects.keys():
                if key.startswith(class_name):
                    objects_to_print.append(str(all_objects[key]))

        print(objects_to_print)

    def do_update(self, args):
        """Update an instance based on the class name and id.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args_list = args.split()
        if not args_list:
            print("** class name missing **")
            return
        if args_list[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return

        all_objects = storage.all()
        key = f"{args_list[0]}.{args_list[1]}"
        if key not in all_objects:
            print("** no instance found **")
            return

        obj = all_objects[key]
        if len(args_list) < 3:
            print("** attribute name missing **")
            return
        if len(args_list) < 4:
            print("** value missing **")
            return

        attr_name = args_list[2]
        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            try:
                attr_value = attr_type(args_list[3])
                setattr(obj, attr_name, attr_value)
                obj.save()
            except ValueError:
                print("** value must be a valid " + str(attr_type))
        else:
            print("** attribute doesn't exist **")

    def do_count(self, line):
        """Retrieve the number of instances of a class.
        Usage: <class name>.count()
        """
        args = line.split('.')
        if len(args) != 2 or args[1] != "count()":
            print("** invalid command **")
            return
        class_name = args[0]
        if class_name == "User":
            class_name = "users"  # Convert to the attribute name in storage
        all_objects = storage.all()
        count = sum(1 for key in all_objects.keys() if key.startswith(class_name))
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
