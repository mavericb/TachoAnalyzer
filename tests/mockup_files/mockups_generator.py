from root.controller.utils.txt_to_list import from_txt_with_newlines_filename_to_list
from root.model.values import Values, TimeValues, FrequencyValues, NonLinearValues


#generate_domain_values_from_tachogram_list(tacho_lst)
from tests import test_constants


def create_mockup_object():
  return Values(TimeValues(1,2), FrequencyValues(3,4), NonLinearValues(5))

def create_mockup_tachograms_list_object():
    filename = test_constants.TACHOGRAM_FILE_MOCKUP
    tacho_lst = from_txt_with_newlines_filename_to_list(filename)
    return list(map(float, tacho_lst))

def create_mockup_fig_object():
    import matplotlib
    matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt

    fig = plt. figure()
    return fig