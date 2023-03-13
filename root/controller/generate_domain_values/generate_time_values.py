import statistics

from root.controller.utils.float_2_digits import float_2_digit
from root.model.values import TimeValues

def generate_time_values(tachograms_list_floats):
    mean = float_2_digit(statistics.mean(tachograms_list_floats))
    sd = float_2_digit(statistics.stdev(tachograms_list_floats))
    return TimeValues(mean, sd)