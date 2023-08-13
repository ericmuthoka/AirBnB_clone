#!/usr/bin/python3
"""
Module for the entry point of the command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Custom command interpreter."""

    prompt = "(hbnb) "

    def do_quit(self, _):
        """Quits the program."""
        print("Goodbye!")
        exit()

    def do_EOF(self, _):
        """Exits the program on Ctrl+D."""
        return self.do_quit(_)

    def do_help(self, _):
        """Displays help information."""
        print("Available commands:")
        for command in self.commands.keys():
            print(f"  {command}")

    def emptyline(self):
        """Does nothing on an empty line."""
        pass

    def help_quit(self):
        """Help for the quit command."""
        print("Quit command to exit the program")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
