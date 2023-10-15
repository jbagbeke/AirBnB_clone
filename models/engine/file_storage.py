#!/usr/bin/python3
"""
Serializes instances to a JSON file and deserializes JSON file to instances
"""
import json
import os
import importlib


class FileStorage:
    """
    Does serialisation to and from a JSON file
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns dictionary __objects

        Args: None
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id

        Args:
            Arg1: (obj) object to set

        Return: None
        """

        name_and_id = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[name_and_id] = obj

    def get_class(self, cls_name):
        """
        Returns name of class stored in dict form

        Args:
            Arg1: (cls_name) Name of class to return
        Return: Appropriate name of class
        """
        try:
            if cls_name == "BaseModel":
                module_name = "base_model"
            else:
                module_name = cls_name.lower()

            module_name = "models." + module_name
            imported_mod = importlib.import_module(module_name)

            return getattr(imported_mod, cls_name)
        except (ImportError, AttributeError):
            return None

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """

        saved_dict = {}

        for key, value in FileStorage.__objects.items():
            saved_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(saved_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                loaded_dict = json.load(file)

                special_dict = {}
                for key, obj in loaded_dict.items():
                    class_name = obj['__class__']
                    cls = self.get_class(class_name)

                    del obj['__class__']
                    if cls is not None:
                        special_dict[key] = cls(**obj)

                FileStorage.__objects = special_dict
