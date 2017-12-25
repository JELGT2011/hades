from unittest import TestCase

from hades.entity.action import Action


class TestAction(TestCase):

    def test_init(self):
        action = Action(timestamp=None, input_event=None, screenshot=None)
        assert action is not None
