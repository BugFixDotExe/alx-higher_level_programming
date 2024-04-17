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

    def to_json(self):
        """to_json a methodthat retrieves a dictionary
        representation of a Student instance"""
        return self.__dict__
