#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Person class; Students and Employees are sub-classes
"""

class Person:

    def __init__(self, first, last):
        self.firstname = first.capitalize()
        self.lastname = last.capitalize()

    def __str__(self):
        return self.firstname + " " + self.lastname

    def __eq__(self, other):
        return (self.firstname == other.firstname) \
            and (self.lastname == other.lastname)

    def is_employed(self):
        return False


class Student(Person):
    "Person who is a student"
    def __init__(self, first, last, school, id):
        # Call Superclass to set common information
        super().__init__(first, last)
        self.school = school
        self.id = id

    def __str__(self):
        # Call Superclass to dispaly common information
        return super().__str__() + ", " + str(self.id) + ' at ' + self.school

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return super().__eq__(other) and (self.id == other.id) and (self.school == other.school)

class Employee(Person):
    "Person who is employed"
    def __init__(self, first, last, company, id):
        # Call Superclass to set common information
        super().__init__(first, last)
        self.id = id
        self.company = company

    def __str__(self):
        # Call Superclass to dispaly common information
        return super().__str__() + ", " + str(self.id) + ' at ' + self.company

    def __eq__(self, other):
        if not isinstance(other, Employee):
            return False
        return super().__eq__(other) and (self.id == other.id) and (self.company == other.company)

    def is_employed(self):
        return True



