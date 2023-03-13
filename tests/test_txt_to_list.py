from unittest import TestCase

from root.controller.utils.txt_to_list import from_txt_with_newlines_filename_to_list


class Test(TestCase):
    def test_from_txt_with_newlines_filename_to_list(self):
        filename = 'mockup_files/007.txt'
        lst = from_txt_with_newlines_filename_to_list(filename)
        #print(from_txt_with_newlines_filename_to_list(filename))
        self.assertEqual(lst[0], 704)