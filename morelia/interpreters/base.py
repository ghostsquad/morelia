# -*- coding: utf-8 -*-
from contracts import ContractsMeta, contract
from abc import abstractmethod


class Interpreter(object):
    __metaclass__ = ContractsMeta

    @contract(name='str')
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    @contract(sensor_data='dict')
    def activate(self, sensor_data):
        pass
