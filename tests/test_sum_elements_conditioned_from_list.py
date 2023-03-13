from unittest import TestCase

from root.controller.utils.sum_elements_conditioned_from_list import sum_elements_conditioned_from_list


class Test(TestCase):
    def test_sum_elements_conditioned_from_list(self):
        lst = [0.1,0.2,0.3,0.4,0.5]
        #print(sum_elements_conditioned_from_list(lst, 0.0, 0.3))
        self.assertEqual(sum_elements_conditioned_from_list(lst, 0.0, 0.3),2)