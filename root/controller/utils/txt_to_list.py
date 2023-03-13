def from_txt_with_newlines_filename_to_list(filename):
    a_file = open(filename)
    file_contents = a_file.read()
    file_contents = extract_numbers(file_contents)
    a_file.close()
    return file_contents

def extract_numbers(test_string):
    res = [int(i) for i in test_string.split() if i.isdigit()]
    #print(res)
    return res
