# coletores/base.py

from abc import ABC, abstractmethod


class ColetorBase(ABC):

    @abstractmethod
    def buscar(self):
        pass
