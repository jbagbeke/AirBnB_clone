#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    A subclass for text based interaction
    Inherits from cmd.Cmd
    """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program

        """
        sys.exit(1)

    def do_EOF(self, arg):
        """
        Command to handle EOF (Ctrl+D or Ctrl+Z) by exiting the console/program
        """
        sys.exit(1)

    def help_quit(self):
        """The help function for Quit """
        print('Quit command to exit the program')
        print("")

    def help_EOF(self):
        """ This is the help function for EOF """
        print("EOF command to exit the program")

    def emptyline(self):
        """
        Executes no command when no input is entered
        """
        pass
    
    def do_create(self, arg):
        """ this is the create command """
        if arg != "":
            if arg == "BaseModel":
                new_class = BaseModel()
                storage.save()
                print(new_class.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_create(self):
        """ This is the help function for create """
        print("create class name")

    def do_show(self, arg):
        """ this is the show command """
        args = arg.split()
        print(args[0])
        if args[0] != "":
            if args[0] == "BaseModel":
                new_class = BaseModel()
                if args[1] != "":
                    if args[1] == new_class.id:
                        print(new_class.__repr__)
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_show(self):
        """ This is the help doc for the show command """
        print("show <classname> <instance-id>")

    def do_destroy(self, arg):
        """ this is the destroy command """
        args = arg.split()
        print(args[0])
        if args[0] != "":
            if args[0] == "BaseModel":
                new_class = BaseModel()
                if args[1] != "":
                    if args[1] == new_class.id:
                        del new_class
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_destroy(self):
        """ This is the help doc for the destroy command """
        print("destroy <classname> <instance-id>")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
