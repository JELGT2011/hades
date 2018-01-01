from unittest import TestCase

from doubles import expect

from hades.controller.output import output_controller
from hades.entity.action import Action, KeyboardActionType


class TestOutputController(TestCase):

    def test_replay_actions(self):
        kwargs = {'key': 'a'}
        action = Action(type_=KeyboardActionType.KEY_DOWN, timestamp=0, kwargs=kwargs)
        expect(output_controller).replay_action(action)
        output_controller.replay_actions([action], 1)

    def test_replay_action(self):
        kwargs = {'key': 'a'}
        action = Action(type_=KeyboardActionType.KEY_DOWN, timestamp=0, kwargs=kwargs)
        expect(output_controller.actuators['keyboard']).press(**kwargs)
        output_controller.replay_action(action)
