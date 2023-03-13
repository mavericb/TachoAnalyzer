from root.controller.generate_domain_values.generate_frequency_values import generate_frequency_values
from root.controller.generate_domain_values.generate_non_linear_values import generate_non_linear_values
from root.controller.generate_domain_values.generate_time_values import generate_time_values
from root.model.values import Values, TimeValues, FrequencyValues, NonLinearValues


def generate_domain_values_from_tachogram_list(tachograms_list):
    tachograms_list_floats = list(map(float, tachograms_list))

    timeValues = generate_time_values(tachograms_list_floats)

    frequencyValues = generate_frequency_values(tachograms_list_floats)

    nonLinearValues = generate_non_linear_values(tachograms_list_floats)

    return Values(TimeValues(timeValues.mean, timeValues.SDNN),
                  FrequencyValues(frequencyValues.lsULF,frequencyValues.lsVLF),
                  NonLinearValues(nonLinearValues.sample_entropy))



