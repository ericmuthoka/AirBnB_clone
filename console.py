#!/usr/bin/python3

"""
This is the entry point of the command interpreter.
"""

import cmd
from models.base_model import BaseModel
from models.user import User  # Import User class
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
        print("The help command shows list of all the available commands.")

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_create(self, args):
        """Create a new instance of BaseModel and save it."""
        if not args:
            print("** class name missing **")
            return
        try:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Show the string representation of an instance."""
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        if args_list[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        all_objects = storage.all()
        key = f"{args_list[0]}.{args_list[1]}"
        if key in all_objects:
            print(all_objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Destroy an instance based on the class name and id."""
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        if args_list[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        all_objects = storage.all()
        key = f"{args_list[0]}.{args_list[1]}"
        if key in all_objects:
            del all_objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances based
        or not on the class name."""
        args_list = args.split()
        all_objects = storage.all()
        objects_to_print = []
        if not args:
            for obj in all_objects.values():
                objects_to_print.append(str(obj))
        elif args_list[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        else:
            for key in all_objects.keys():
                if key.startswith(args_list[0]):
                    objects_to_print.append(str(all_objects[key]))
        print(objects_to_print)

    def do_update(self, args):
        """Update an instance based on the class name and id."""
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        if args_list[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        all_objects = storage.all()
        key = f"{args_list[0]}.{args_list[1]}"
        if key in all_objects:
            if len(args_list) < 3:
                print("** attribute name missing **")
                return
            if len(args_list) < 4:
                print("** value missing **")
                return
            obj = all_objects[key]
            setattr(obj, args_list[2], args_list[3])
            obj.save()
        else:
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
