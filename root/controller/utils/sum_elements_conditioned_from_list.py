def sum_elements_conditioned_from_list(lst, min,max):
    return sum(condition(x, min, max) for x in lst)

def condition(x, min, max):
  return x >=min and x< max

