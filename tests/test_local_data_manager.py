from unittest import TestCase

from root import constants
import test_constants
from root.controller.utils.local_data_manager.local_data_manager import dump_filename, load_data


class Test(TestCase):
    class Test(TestCase):
        def test_dump_filename(self):
            dump_filename(test_constants.FILENAME_DATA_MOCKUP, 'mockup_files/filename.data')
            self.assertTrue(load_data('mockup_files/filename.data'), test_constants.FILENAME_DATA_MOCKUP)


class Test(TestCase):
    def test_load_filename(self):
        self.assertTrue(load_data(constants.FILENAME_DATA), constants.FILENAME_DATA)

