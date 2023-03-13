from root import constants

def refresh_domain_values(window, values):
    window[constants.MEAN_KEY].update(values.timeValues.mean)
    window[constants.SDNN_KEY].update(values.timeValues.SDNN)
    window[constants.lsULF_KEY].update(values.frequencyValues.lsULF)
    window[constants.lsVLF_KEY].update(values.frequencyValues.lsVLF)
    window[constants.Sample_Entropy_KEY].update(values.nonLinearValues.sample_entropy)

