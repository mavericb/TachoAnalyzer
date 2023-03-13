import PySimpleGUI as sg

from root.controller.listener.listener import activate_listener
from root.vista.homepage_layout import homepage_layout


def main():
    window = homepage_layout(sg)
    activate_listener(window, sg)

if __name__ == "__main__":
    main()

