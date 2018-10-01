from unittest import TestCase

from spacer import Spacer


class TestSpacer(TestCase):
    def test_space_out(self):
        word_dict = {['be', 'than', 'hand', 'bat', 'bed', 'bath', 'and', 'beyond']}
        self.assertEqual('bed bath and beyond', Spacer.space_out('bedbathandbeyond', word_dict))
