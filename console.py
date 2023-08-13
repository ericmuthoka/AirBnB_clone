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
        elif line not in ["BaseModel", "State", "City", "Amenity", "Place", "Review"]:
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
        elif args[0] not in ["BaseModel", "State", "City", "Amenity", "Place", "Review"]:
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

    # Implement other commands (destroy, update, all) for other classes

if __name__ == "__main__":
    HBNBCommand().cmdloop()
