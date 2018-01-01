from enum import Enum as Enum_

from schematics import Model


class Entity(Model):
    pass


class Enum(Enum_):

    def __str__(self):
        return self.name
