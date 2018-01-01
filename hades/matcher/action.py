from hades.entity.action import Action
from hades.lib import get_logger
from hades.matcher.base import Matcher

logger = get_logger(__name__)


class ActionMatcher(Matcher):

    def __init__(self, isjunk=None, a='', b='', autojunk=False):
        super().__init__(isjunk=isjunk, a=a, b=b, autojunk=autojunk)
        self.actions = list()

    def append(self, action: Action):
        from hades.controller.input import input_controller
        self.actions.append(action)
        if len(self.actions) < 2:
            return
        mid = int(len(self.actions) / 2)
        action_types = [action.type_ for action in self.actions]
        left, right = action_types[mid:], action_types[:mid]
        self.set_seqs(left, right)
        if self.found_match:
            logger.info('found match')
            logger.info('opcodes: {}'.format(self.get_opcodes()))
            input_controller.stop()
