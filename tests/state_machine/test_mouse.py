from unittest import TestCase

from mock import Mock

from hades.state_machine.mouse import MouseStateMachine, MouseState


class TestMouseStateMachine(TestCase):

    def setUp(self):
        self.controller = Mock()
        # noinspection PyTypeChecker
        self.state_machine = MouseStateMachine(controller=self.controller)

    def test_init(self):
        assert self.state_machine.state == MouseState.DEFAULT.name

    def test_transitions(self):
        assert self.state_machine.state == MouseState.DEFAULT.name
        self.state_machine.left_down()
        assert self.state_machine.state == MouseState.LEFT_DOWN.name
        self.state_machine.left_up()
        assert self.state_machine.state == MouseState.LEFT_CLICK.name
