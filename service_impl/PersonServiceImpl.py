# -*- coding: utf-8 -*-
# @Time    : 2021/8/28 9:07
# @Author  : 王天赐
# @Email   : 15565946702@163.com
# @File    : PersonServiceImpl.py
# @Software: PyCharm
from random import random

from thrift_generator import ttypes
from thrift_generator.PersonService import Iface


class PersonServiceImpl(Iface):
    def getPersonByUsername(self, username):
        """
        Parameters:
         - username

        """
        print("py : getPersonByUsername")

        person = ttypes.Person()
        person.username = username
        person.age = int(random())
        person.married = False

        return person

    def savePerson(self, person):
        """
        Parameters:
         - person

        """
        print(person.username)
        print(person.age)
        print(person.married)
