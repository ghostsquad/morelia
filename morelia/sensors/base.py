from contracts import ContractsMeta, contract
from abc import abstractmethod


class Sensor(object):
    __metaclass__ = ContractsMeta

    @contract(name='str')
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def activate(self):
        pass
