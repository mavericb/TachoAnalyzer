import antropy as ant
from root.model.values import NonLinearValues

def generate_non_linear_values(tachograms_list_floats):
    sample_entropy = ant.sample_entropy(tachograms_list_floats)

    return NonLinearValues(sample_entropy)