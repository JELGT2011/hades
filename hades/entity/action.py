from hades.entity.base import Entity


class Action(Entity):

    def __init__(self, timestamp, input_event, screenshot):
        super().__init__()
        self.timestamp = timestamp
        self.input_event = input_event
        self.screenshot = screenshot
