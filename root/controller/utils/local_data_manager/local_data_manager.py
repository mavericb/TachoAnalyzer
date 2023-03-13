from root import constants
import pickle

def dump_data(dataset, output_file_with_folder):
    outputFile = output_file_with_folder
    fw = open(outputFile, 'wb')
    pickle.dump(dataset, fw)
    fw.close()

def load_data(inputFile_with_folder):
    inputFile = inputFile_with_folder
    fd = open(inputFile, 'rb')
    dataset = pickle.load(fd)
    #fd.close()
    return dataset

def dump_filename(filename, filename_data):
    return dump_data(filename, filename_data)


def load_filename():
    return load_data(constants.FILENAME_DATA)

def dump_export_object(export_object):
    return dump_data(export_object, constants.VALUES_OBJECT_DATA)

def load_values_object():
    return load_data(constants.VALUES_OBJECT_DATA)

