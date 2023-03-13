class Values:
  def __init__(self, timeValues, frequencyValues, nonLinearValues):
    self.timeValues = timeValues
    self.frequencyValues = frequencyValues
    self.nonLinearValues = nonLinearValues

  def get_list_names(self):
    return ['mean','SDNN','lsULF','lsVLF','sample_entropy']

  def get_list_values(self):
    return [self.timeValues.mean,self.timeValues.SDNN,
            self.frequencyValues.lsULF,self.frequencyValues.lsVLF,
            self.nonLinearValues.sample_entropy]

def create_mockup_object():
  return Values(TimeValues(1,2), FrequencyValues(3,4), NonLinearValues(5))

class TimeValues:
  def __init__(self, mean, SDNN):
    self.mean = mean
    self.SDNN = SDNN

class FrequencyValues:
  def __init__(self, lsULF, lsVLF):
    self.lsULF = lsULF
    self.lsVLF = lsVLF

class NonLinearValues:
  def __init__(self, sample_entropy):
    self.sample_entropy = sample_entropy

