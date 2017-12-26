from unittest import TestCase

from mock import Mock

from hades.matcher.base import SequenceMatcher


class TestBase(TestCase):

    def setUp(self):
        self.matcher = SequenceMatcher()

    def test_insert_iteration(self):
        types = [0, 1, 1]
        iterations = [Mock(type_=type_) for type_ in types]

        self.matcher.insert_iteration(iterations)
        assert self.matcher.a == ''
        assert self.matcher.b == types
        assert not self.matcher.found_match

        self.matcher.insert_iteration(iterations)
        assert self.matcher.a == types
        assert self.matcher.b == types
        assert self.matcher.found_match
