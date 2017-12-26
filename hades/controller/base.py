from abc import ABC, abstractmethod

from hades.entity.action import Action
from hades.entity.event import Event


class Controller(ABC):

    def __init__(self):
        self.actions = list()
        self.events = list()
        self.keyboard_listener = None
        self.mouse_listener = None
        self.listeners = list()
        self.keyboard_state_machine = None
        self.mouse_state_machine = None

    @abstractmethod
    def register_event(self, event: Event):
        pass

    @abstractmethod
    def register_action(self, action: Action):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @property
    @abstractmethod
    def running(self):
        pass
