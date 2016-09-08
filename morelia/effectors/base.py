# -*- coding: utf-8 -*-
from contracts import ContractsMeta, contract
from abc import abstractmethod


class Effector(object):
    __metaclass__ = ContractsMeta

    @contract(name='str')
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    @contract(input_data='dict')
    def activate(self, input_data):
        pass
