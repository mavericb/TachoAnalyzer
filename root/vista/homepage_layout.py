from root import constants

def homepage_layout(sg):
    file_list_column = [
        [
            sg.Button(constants.ANALYZE_A_TACHOGRAM, size=(18, 1)),
            sg.Button(constants.EXPORT_RESULTS, size=(18, 1), disabled=True, disabled_button_color=('grey', 'white'), )
        ],
        [sg.Text('_' * 70)],
        [sg.Image(key=constants.IMAGE_KEY)],

    ]

    image_viewer_column = [
        [sg.Text('Time-domain features')],
        [sg.Text('Mean')],
        [sg.Text(key=constants.MEAN_KEY)],
        [sg.Text('SDNN')],
        [sg.Text(key=constants.SDNN_KEY)],
        [sg.Text('_' * 30)],


        [sg.Text('Frequency-domain features')],
        [sg.Text('lsULF')],
        [sg.Text(key=constants.lsULF_KEY)],
        [sg.Text('lsVLF')],
        [sg.Text(key=constants.lsVLF_KEY)],
        [sg.Text('_' * 30)],

        [sg.Text('Nonlinear features')],
        [sg.Text('Sample Entropy')],
        [sg.Text(key=constants.Sample_Entropy_KEY)],
        [sg.Text(' ' * 30)],

    ]

    layout = [
        [
            sg.Column(file_list_column,size= (400,360),vertical_alignment = 'top'),
            sg.VSeperator(),
            sg.Column(image_viewer_column),
        ]
    ]

    window = sg.Window(constants.PROGRAM_NAME, layout)
    return window