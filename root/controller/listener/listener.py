from root import constants
from root.controller.listener.events.export_event.export_event import export_event
from root.controller.listener.events.analyze_event.analyze_event import analyze_event

def activate_listener(window, sg):
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == constants.ANALYZE_A_TACHOGRAM:
            if(analyze_event(sg, window)):
                window.Element(constants.EXPORT_RESULTS).Update(disabled=False)

        if event == constants.EXPORT_RESULTS:
            if(export_event(sg)):
                sg.popup('File successfully exported!')

    window.close()


