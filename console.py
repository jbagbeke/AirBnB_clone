#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    A subclass for text based interaction
    Inherits from cmd.Cmd
    """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program

        """
        return True

    def do_EOF(self, line):
        """
        Command to handle EOF (Ctrl+D or Ctrl+Z) by exiting the console/program
        """
        print("")
        return True

    def emptyline(self):
        """
        Executes no command when no input is entered
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
