from unittest import TestCase
from root.controller.generate_domain_values.generate_non_linear_values import generate_non_linear_values
from mockup_files.mockups_generator import create_mockup_tachograms_list_object


class Test(TestCase):
    def test_generate_non_linear_values(self):
        non_linear_values = generate_non_linear_values(create_mockup_tachograms_list_object())
        #print(str(non_linear_values.sample_entropy))
        self.assertEqual(0.6417940382547795, non_linear_values.sample_entropy)
