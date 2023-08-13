#!/usr/bin/python3
"""
This is the entry point of the command interpreter.
"""

import cmd

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
