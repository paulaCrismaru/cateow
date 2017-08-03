from __future__ import absolute_import

import unittest


from cateow import utils
from cateow.unittests import testutils


class TestUtils(unittest.TestCase):

    def test_split_text_in_lines(self):
        self.assertEqual(
            testutils.EXPECTED_TEXT_1_LINE,
            utils.split_text_in_lines(testutils.TEXT_1_LINE))
        for line in testutils.EXPECTED_TEXT_1_LINE:
            self.assertTrue(len(line) <= utils.constants.MAX_LEN_LINE)

        self.assertEqual(
            testutils.EXPECTED_TEXT_2_LINES,
            utils.split_text_in_lines(testutils.TEXT_2_LINES))
        for line in testutils.EXPECTED_TEXT_2_LINES:
            self.assertTrue(len(line) <= utils.constants.MAX_LEN_LINE)

        self.assertEqual(
            testutils.EXPECTED_TEXT_MORE_LINES,
            utils.split_text_in_lines(testutils.TEXT_MORE_LINES))
        for line in testutils.EXPECTED_TEXT_MORE_LINES:
            self.assertTrue(len(line) <= utils.constants.MAX_LEN_LINE)

    def test_make_balloon(self):
        self.assertEqual(
            testutils.ONE_LINE_BALLOON,
            utils.make_balloon(testutils.TEXT_1_LINE))
        self.assertEqual(
            testutils.TWO_LINE_BALLOON,
            utils.make_balloon(testutils.TEXT_2_LINES))
        self.assertEqual(
            testutils.MULTI_LINE_BALLOON,
            utils.make_balloon(testutils.TEXT_MORE_LINES))

    def test_escape_character(self):
        text = "{}{}{}{}{}"
        self.assertEqual(
            "{}{}{}{}}{}}",
            utils.escape_character(text, '}', '}}'))
        self.assertEqual(
            "{}{}}{}}{}}{}}",
            utils.escape_character(text, '}', '}}', 1))

    def test_get_last_space_index(self):
        self.assertEqual(4, utils.get_last_space_index("fake text"))
        self.assertEqual(4, utils.get_last_space_index("fake fake text", 5))
