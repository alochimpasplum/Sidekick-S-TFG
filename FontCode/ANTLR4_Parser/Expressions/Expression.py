from abc import ABC, abstractmethod


class Expression(ABC):

    @abstractmethod
    def to_string(self):
        pass
