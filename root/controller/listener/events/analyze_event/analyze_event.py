import os

from root import constants
from root.controller.utils import txt_to_list
from root.controller.utils.local_data_manager.local_data_manager import dump_filename, dump_export_object
from root.vista.draw_tachogram_image import draw_tachogram_image
from root.controller.generate_domain_values.update_domain_values import update_domain_values


def analyze_event(sg, window):
    filename = sg.PopupGetFile(constants.SELECT_A_TACHOGRAM_FILE)
    if filename:
        try:
            check_format(filename)
            dump_filename(filename, constants.FILENAME_DATA)
            return load_tachogram_and_values_event(filename, window)
        except Exception as error:
            sg.Popup(error)

    return False

def load_tachogram_and_values_event(filename, window):
    if os.path.exists(filename):
        tachograms_list = txt_to_list.from_txt_with_newlines_filename_to_list(filename)

        image = draw_tachogram_image(tachograms_list, window)
        image.save(constants.PLOT_IMAGE, format="PNG")

        values = update_domain_values(tachograms_list, window)

        dump_export_object(values)

        return True

    return False


def check_format(filename):
    name, extension = os.path.splitext(filename)
    if(extension!='.txt' and extension!='.csv'):
        raise Exception('Bad format file!')

