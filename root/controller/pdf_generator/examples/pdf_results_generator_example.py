from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def pdf_results_generator():
    doc = SimpleDocTemplate("form_letter.pdf",pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)
    Story=[]

    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    ptext = 'Exported results'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    logo = "python_logo.png"
    im = Image(logo, 2*inch, 2*inch)
    Story.append(im)
    Story.append(Spacer(1, 12))

    features = ['mean','sdnn', 'ilvs', 'uls', 'st']
    measures = [1,2,3,4,5]
    i = 0
    while i < len(features):
        ptext = features[i] + ': '+ str(measures[i])
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 12))
        i+=1

    Story.append(Spacer(1, 12))

    ptext = 'Thank you very much for using EBTacho, you\'re awesome :)'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 24))
    ptext = 'Bye!'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    ptext = 'Eric Boniardi'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    doc.build(Story)