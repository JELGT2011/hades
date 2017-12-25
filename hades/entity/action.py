from hades.entity.base import Entity


class Action(Entity):

    def __init__(self, timestamp=None, input_event=None, screenshot=None):
        super().__init__()
        self.timestamp = timestamp
        self.input_event = input_event
        self.screenshot = screenshot

    def __hash__(self):
        return hash(self.timestamp)
