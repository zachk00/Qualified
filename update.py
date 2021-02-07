from docx import Document
from docx.shared import Pt
import datetime


def read_file(filename):
    doc = Document(filename)
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(11)
    oldtext = ""

    for paragraph in doc.paragraphs:
        if "_Date_" in paragraph.text:
            oldtext = paragraph.text
            paragraph.text = oldtext.replace("_Date_", get_date(), 1)
            paragraph.style = doc.styles['Normal']
            doc.save('new.docx')


def get_date():
    current_time = datetime.datetime.now()
    day = str(current_time.day)
    month = str(current_time.month)
    year = str(current_time.year)
    date = month + "/" + day + "/" + year
    return date
