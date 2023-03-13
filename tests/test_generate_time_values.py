from unittest import TestCase

from root.controller.generate_domain_values.generate_time_values import generate_time_values
from mockup_files.mockups_generator import create_mockup_tachograms_list_object


class Test(TestCase):
    def test_generate_time_values(self):
        time_values = generate_time_values(create_mockup_tachograms_list_object())
        #print(str(time_values.mean))
        self.assertEqual(752.44,time_values.mean)