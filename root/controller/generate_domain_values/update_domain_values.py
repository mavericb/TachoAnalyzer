from root.controller.generate_domain_values.generate_domain_values import generate_domain_values_from_tachogram_list
from root.vista.refresh_domain_values import refresh_domain_values


def  update_domain_values(tachograms_list, window):
    values = generate_domain_values_from_tachogram_list(tachograms_list)
    refresh_domain_values(window, values)

    return values
