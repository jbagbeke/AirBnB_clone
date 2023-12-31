#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""
import cmd
import re
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

    def _UpdateDict(self, line, diction):
        """ Updates several attributes passed in a dictionary """

        for key, value in diction.items():
            line_cpy = line[7:]
            line_cpy = line_cpy + " " + str(key) + " " + str(value)
            self.do_update(line_cpy)

        return

    def onecmd(self, line):
        """
        Preprocess the input line before passing it to the command processor
        """
        line_copy = line
        pattern = r'([BURPACS]\w+)\.(\w+)()'
        matches = re.search(pattern, line)
        if matches is not None:
            line = str(matches.group(2)) + " " + str(matches.group(1))

            if matches.group(2) in ("show", "destroy"):
                patt_ern = r'\("?(.*?)"?\)'
                new_match = re.search(patt_ern, line_copy)

                if new_match is not None:
                    line = line + " " + str(new_match.group(1))
            elif matches.group(2) == "update":
                match_one = re.search(r'\("?(.*?)"?,\s(\{.*?)\)', line_copy)

                pat_two = r'\("?(.*?)"?,\s"?(.*?)"?,\s"?(.*?)"?\)'
                match_two = re.search(pat_two, line_copy)

                if match_one:
                    line = line + " " + str(match_one.group(1))
                    self._UpdateDict(line, eval(match_one.group(2)))
                    return
                elif match_two:
                    line = line + " " + str(match_two.group(1)) + " "
                    line = line + str(match_two.group(2)) + " "
                    line = line + str(match_two.group(3))

        return super().onecmd(line)

    def do_EOF(self, line):
        """Handles EOF (Ctrl+D or Ctrl+Z) by exiting the console"""
        sys.exit(1)

    def do_quit(self, line):
        """ Quit command to exit the program """
        sys.exit(1)

    def do_create(self, line):
        """ this is the create command """
        lines = line.split()

        if len(lines) > 0:
            if self._CheckClass(lines[0]):
                new_class = storage.get_class(lines[0])
                new_instance = new_class()
                storage.save()
                print(new_instance.id)
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

    def _ExecuteCommand(self, line, function):
        """Prints str representation of instance based on class name and id"""
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
                        function(loaded_obj, name_and_id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Prints str representation of instance based on class name and id"""

        def show_it(loaded_obj, name_and_id):
            """ Defines final command in show method """
            print(loaded_obj[name_and_id])

        self._ExecuteCommand(line, show_it)

    def do_count(self, line):
        """ Retrieves the number of instances of a class """

        lines = line.split()
        loaded_obj = storage.all()
        instance = 0

        if self._CheckClass(lines[0]):
            for key in loaded_obj.keys():
                name = key.split(".")
                if lines[0] == name[0]:
                    instance += 1
            print(instance)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Prints str representation of instance based on class name and id"""

        def destroy_it(loaded_obj, name_and_id):
            """ Defines final command for destroy method """
            del loaded_obj[name_and_id]
            storage.save()

        self._ExecuteCommand(line, destroy_it)

    def do_all(self, line):
        """
        Prints all str representation of instances based or not on class name
        """
        lines = line.split()
        loaded_obj = storage.all()

        obj_list = []

        if len(lines) == 0:
            for key in loaded_obj.keys():
                obj_list.append(str(loaded_obj[key]))
            print(obj_list)
        elif len(lines) > 0:
            if self._CheckClass(lines[0]):
                for key in loaded_obj.keys():
                    name_and_id = key.split(".")
                    if name_and_id[0] == lines[0]:
                        obj_list.append(str(loaded_obj[key]))
                print(obj_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates instance using class name and id by adding/updating attribute
        """
        lines = line.split()

        def update_it(loaded_obj, name_and_id):
            """ Defines final command for the update method """

            if len(lines) < 3:
                print("** attribute name missing **")
            elif len(lines) < 4:
                print("** value missing **")
            else:
                obj = loaded_obj[name_and_id]
                try:
                    val_typecast = type(getattr(obj, lines[2]))(lines[3])
                    setattr(obj, lines[2], val_typecast)
                except AttributeError:
                    obj.__dict__[lines[2]] = lines[3]
                storage.save()

        self._ExecuteCommand(line, update_it)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
