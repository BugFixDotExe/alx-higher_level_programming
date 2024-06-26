#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A module that  that retrieves
a dictionary representation of a
Student instance """


class Student:
    """A class Student that defines a student """
    def __init__(self, first_name, last_name, age):
        """__init__ the constructor of class"""
        """
            Args:
                first_name (string): first arg
                second_name (string): second arg
                age (int): third arg
            Returns:
                a dictionary representation of a Student
                instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        match = dict()
        """to_json a method that retrieves a dictionary
        representation of a Student instance"""
        if attrs is not None:
            for token in attrs:
                if token in self.__dict__:
                    match[token] = self.__dict__[token]
            return match
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """reload_from_json """
        """a function that replaces all attributes
        of the Student instance
        Args:
            json (dict) containing key value
        """
        self.first_name = json.get("first_name")
        self.last_name = json.get("last_name")
        self.age = json.get("age")
