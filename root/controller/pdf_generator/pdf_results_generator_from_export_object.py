from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

from root import constants


def pdf_results_generator_from_export_object(destination_file, export_object):
    doc = SimpleDocTemplate(destination_file, pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)
    Story = []

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    ptext = 'Exported results'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    plot_image = constants.PLOT_IMAGE
    im = Image(plot_image, 2 * inch, 2 * inch)

    Story.append(im)
    Story.append(Spacer(1, 12))

    features = export_object.get_list_names()
    measures = export_object.get_list_values()


    i = 0
    while i < len(features):
        ptext = features[i] + ': ' + str(measures[i])
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 12))
        i += 1

    Story.append(Spacer(1, 12))

    ptext = 'Thank you very much for using TachoE, you\'re awesome :)'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
    ptext = 'Bye,'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    ptext = 'Eric'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    doc.build(Story)