import unittest

from hades.state_machine.mouse import MouseStateMachine, MouseState


class TestMouseStateMachine(unittest.TestCase):

    def setUp(self):
        self.state_machine = MouseStateMachine()

    def test_init(self):
        assert self.state_machine.state == MouseState.DEFAULT.name

    def test_transitions(self):
        assert self.state_machine.state == MouseState.DEFAULT.name
        self.state_machine.left_down()
        assert self.state_machine.state == MouseState.LEFT_DOWN.name
        self.state_machine.left_up()
        assert self.state_machine.state == MouseState.SINGLE_CLICKED.name
