import abc
import enum


class Entity(abc.ABC):
    pass


class Enum(enum.Enum):

    def __str__(self):
        return self.name
