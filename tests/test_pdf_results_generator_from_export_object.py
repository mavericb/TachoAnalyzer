from unittest import TestCase
from pathlib import Path

from root.controller.pdf_generator.pdf_results_generator_from_export_object import pdf_results_generator_from_export_object
from mockup_files.mockups_generator import create_mockup_object


class Test(TestCase):
    def test_pdf_results_generator_from_export_object(self):
        #create mockup export object
        mockup_values = create_mockup_object()

        output_file = 'mockup_files/pdf_output_test.pdf'

        #create the pdf
        filename = str(Path(output_file))
        pdf_results_generator_from_export_object(filename, mockup_values)

        #laod and read the pdf and test if found the vlaue created

        import PyPDF2

        # creating a pdf file object
        pdfFileObj = open(output_file, 'rb')

        # creating a pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # creating a page object
        pageObj = pdfReader.getPage(0)

        # extracting text from page
        #print(pageObj.extractText())
        text = pageObj.extractText()

        # print(text.find('mean') != -1)
        # print(text.find('1') != -1)

        self.assertTrue(text.find('mean') != -1 and text.find('1') != -1)

        # closing the pdf file object
        pdfFileObj.close()

        import os
        if os.path.exists(output_file):
            os.remove(output_file)
        else:
            print("The file does not exist")