from __future__ import absolute_import

import os
import unittest

try:
    import unittest.mock as mock
except ImportError:
    import mock


from cateow import utils
from cateow import cateow as cateow_py
from cateow.unittests import test_utils


class TestCateow(unittest.TestCase):

    @mock.patch('cateow.cateow.escape_kitty_template')
    @mock.patch('cateow.utils.make_balloon')
    def test_cateow(self, mock_make_balloon,
                    mock_escape):
        mock_make_balloon.return_value = "fake_balloon"
        mock_escape.return_value = test_utils.VALID_KITTY_TEMPLATE
        result = cateow_py.cateow(None, None)
        expected_result = test_utils.VALID_KITTY_TEMPLATE.format(
            balloon=mock_make_balloon.return_value, way="\\")

        self.assertEqual(result, expected_result)

    @mock.patch('cateow.cateow.escape_kitty_template')
    @mock.patch('cateow.utils.make_balloon')
    def test_cateow_format_fails(self, mock_make_balloon,
                                 mock_escape):
        mock_escape.return_value = test_utils.INVALID_KITTY_TEMPLATE
        with self.assertRaises(utils.CateowException) as ex:
            cateow_py.cateow(None, None)
        self.assertEqual(str(ex.exception), "Kitty formating failed :(")

    def test_get_meanie_none(self):
        fake_meanies = ['fake meanie 1', 'fake meanie 2', 'fake meanie 3']
        with mock.patch('cateow.cateow.open', create=True) as mock_open:
            mock_open.return_value.__enter__().readlines.return_value = \
                fake_meanies
            result = cateow_py.get_meanie(None)
        mock_open.return_value.__enter__().readlines.assert_called_once_with()
        self.assertEqual(mock_open.call_count, 1)
        self.assertTrue(result in fake_meanies)

    @mock.patch('cateow.cateow.os.getcwd')
    @mock.patch('cateow.cateow.os.path.isfile')
    @mock.patch('cateow.cateow.os.path.isabs')
    def test_get_meanie_exception(self, mock_is_abs,
                                  mock_is_file, mock_cwd):
        mock_cwd.return_value = "fake cwd"
        mock_is_abs.return_value = False
        mock_is_file.return_value = False
        fake_path = "fake path"
        expected_path = os.sep.join(
            [mock_cwd.return_value, fake_path])
        with self.assertRaises(utils.CateowException) as ex:
            cateow_py.get_meanie(fake_path)
        self.assertEqual(str(ex.exception),
                         "No such file: '{}'".format(expected_path))

    @mock.patch('cateow.cateow.os.path.isdir')
    def test_get_kitty_none(self, mock_is_dir):
        mock_is_dir.return_value = True
        fake_kitty = "fake kitty"
        with mock.patch('cateow.cateow.open', create=True) as mock_open:
            mock_open.return_value.__enter__().read.return_value = fake_kitty
            kitty = cateow_py.get_kitty(None)
        mock_open.return_value.__enter__().read.assert_called_once_with()
        self.assertEqual(mock_open.call_count, 1)
        self.assertEqual(kitty, fake_kitty)

    @mock.patch('cateow.cateow.os.getcwd')
    @mock.patch('cateow.cateow.os.path.isfile')
    @mock.patch('cateow.cateow.os.path.isabs')
    def test_get_kitty_exception(self, mock_is_abs,
                                 mock_is_file, mock_cwd):
        mock_cwd.return_value = "fake cwd"
        mock_is_abs.return_value = False
        mock_is_file.return_value = False
        fake_path = "fake path"
        with self.assertRaises(utils.CateowException) as ex:
            cateow_py.get_kitty(fake_path)
        expected_path = os.sep.join(
            [mock_cwd.return_value, fake_path])
        self.assertEqual(str(ex.exception),
                         "No such file: '{}'".format(expected_path))

    def test_escape_kitty_template(self):
        expected_result = "{not}{not}{not}{{escaped}}{{escaped}}"
        kitty_template = "{not}{not}{not}{escaped}{escaped}"
        result = cateow_py.escape_kitty_template(kitty_template)
        self.assertEqual(result, expected_result)
