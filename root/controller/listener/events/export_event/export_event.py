from root import constants
from root.controller.exporter.exporter import exporter


def export_event(sg):
    folder_name = sg.PopupGetFolder(constants.SELECT_OUTPUT_FOLDER)
    if folder_name:
        exporter(folder_name)
        return True
    return False
