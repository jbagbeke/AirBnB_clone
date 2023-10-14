#!/usr/bin/python3
"""
The base module for other classes
It defines all common attributes/methods for other classes
"""
from models import storage
import uuid
from datetime import datetime


class BaseModel:
    """
    Defines attrubutes and models that will be common to other classes
    and will be inherited by other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Instantiates common attributes

        Args:
            Arg1: (args) allows variable # of non-keyworded args to be passed
            Arg2: (kwargs) allows variable # of keyworded args to be passed
        """

        if kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    key_val = datetime.fromisoformat(value)
                    setattr(self, key, key_val)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        Returns string representation of desired output
        """
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def save(self):
        """
        Updates public instance attribute updated_at with current datetime

        Args: None

        Return: None
        """

        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance

        Args: None

        Return: Dict containing key/values of the instance
        """

        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__

        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()

        return dict_copy
