from unittest import TestCase

from root.controller.generate_domain_values.generate_frequency_values import generate_frequency_values
from mockup_files.mockups_generator import create_mockup_tachograms_list_object


class Test(TestCase):
    def test_generate_frequency_values(self):
        frequency_values = generate_frequency_values(create_mockup_tachograms_list_object())
        # print(str(frequency_values.lsVLF))
        self.assertEqual(201, frequency_values.lsVLF)

