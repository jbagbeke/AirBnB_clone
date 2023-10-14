#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """
    A subclass for text based interaction
    Inherits from cmd.Cmd
    """

    prompt = "(hbnb) "

    def help_show(self):
        """ This is the help doc for the show command """
        print("show <classname> <instance-id>")

    def help_create(self):
        """ This is the help function for create """
        print("create class name")

    def help_quit(self):
        """The help function for Quit """
        print('Quit command to exit the program')
        print("")

    def help_destroy(self):
        """ This is the help doc for the destroy command """
        print("destroy <classname> <instance-id>")

    def help_EOF(self):
        """ This is the help function for EOF """
        print("EOF command to exit the program")

    def emptyline(self):
        """ Executes no command when no input is entered """
        pass

    def do_EOF(self, arg):
        """ Command to handle EOF (Ctrl+D or Ctrl+Z) by exiting the console/program"""
        sys.exit(1)

    def do_quit(self, line):
        """ Quit command to exit the program """
        sys.exit(1)
    
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

    def _CheckClass(self, line):
        """ Checks if a class exists """
        classes = [
                "BaseModel", "User", "State", "City",
                "Amenity", "Place", "Review"
                ]

        if line not in classes:
            return False
        else:
            return True

   def do_show(self, line):
        """ Prints the string representation of an instance based on the class name and id"""
        lines = line.split()

        if len(lines) == 0:
            print("** class name missing **")
        else:
            if self._CheckClass(lines[0]):
                if len(lines) == 1:
                    print("** instance id missing **")
                else:
                    loaded_obj = storage.all()
                    name_and_id = str(lines[0]) + "." + str(lines[1])

                    if name_and_id not in loaded_obj.keys():
                        print("** no instance found **")
                    else:
                        print(loaded_obj[name_and_id])
            else:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """ Prints the string representation of an instance based on the class name and id"""
        lines = line.split()

        if len(lines) == 0:
            print("** class name missing **")
        else:
            if self._CheckClass(lines[0]):
                if len(lines) == 1:
                    print("** instance id missing **")
                else:
                    storage.reload()
                    loaded_obj = storage.all()
                    name_and_id = str(lines[0]) + "." + str(lines[1])

                    if name_and_id not in loaded_obj.keys():
                        print("** no instance found **")
                    else:
                        del loaded_obj[name_and_id]
                        FileStorage.__objects = loaded_obj
                        storage.save()
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
