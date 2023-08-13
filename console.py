import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def do_help(self, arg):
        """Display help message"""
        super().do_help(arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
