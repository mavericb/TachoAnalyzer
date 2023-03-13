from root.controller.pdf_generator.pdf_results_generator_from_export_object import pdf_results_generator_from_export_object
from root.controller.utils.local_data_manager.local_data_manager import load_filename, load_values_object
import os

def exporter(folder_name):
    extended_filename = load_filename()
    base_filename = os.path.basename(extended_filename)
    destination_file = os.path.join(folder_name, base_filename).replace('.txt','') + '.pdf'

    values_object = load_values_object()

    pdf_results_generator_from_export_object(destination_file, values_object)
