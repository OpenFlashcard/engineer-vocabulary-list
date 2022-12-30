from abc import ABCMeta, abstractclassmethod, abstractproperty
from model import TextFormatter


class Item(metaclass=ABCMeta):
    @abstractproperty
    def formatted_text():
        raise NotImplementedError

    @abstractclassmethod
    def format(self, formatter: TextFormatter = None):
        raise NotImplementedError
