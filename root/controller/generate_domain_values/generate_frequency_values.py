from root import constants
from root.controller.utils.sum_elements_conditioned_from_list import sum_elements_conditioned_from_list
import numpy as np
from root.model.values import FrequencyValues


def generate_frequency_values(listOfFloats):
    from astropy.timeseries import LombScargle
    t = range(0, len(listOfFloats))
    y = np.array(listOfFloats)
    frequency, power = LombScargle(t, y).autopower()

    lsULF = sum_elements_conditioned_from_list(frequency, constants.MIN_lsULF, constants.MAX_lsULF)
    lsVLF = sum_elements_conditioned_from_list(frequency, constants.MIN_lsVLF, constants.MAX_lsVLF)

    return FrequencyValues(lsULF, lsVLF)
