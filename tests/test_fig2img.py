from unittest import TestCase

from root.controller.utils.fig2img import fig2img
from mockup_files.mockups_generator import create_mockup_fig_object


class Test(TestCase):
    def test_fig2img(self):
        fig = create_mockup_fig_object()
        #print(type(fig2img(fig)))
        self.assertEqual('<class \'PIL.Image.Image\'>', str(type(fig2img(fig))))