from unittest import TestCase

from root.controller.utils.float_2_digits import float_2_digit


class Test(TestCase):
    def test_float_2_digit(self):
        #print(float_2_digit(0.013))
        self.assertEqual(float_2_digit(0.013), 0.01)