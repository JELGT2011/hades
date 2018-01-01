from difflib import SequenceMatcher

from hades.lib import get_logger

logger = get_logger(__name__)

MINIMUM_CONFIDENCE = 0.8


class Matcher(SequenceMatcher):

    @property
    def found_match(self):
        return self.ratio() > MINIMUM_CONFIDENCE
