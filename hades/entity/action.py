from hades.entity import Entity


class Action(Entity):

    def __init__(self, input_event, screenshot):
        super(Entity, self).__init__()
        self.input_event = input_event
        self.screenshot = screenshot
