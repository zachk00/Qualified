from docx import Document
from docx.shared import Pt
import datetime


# only pass a copy of the file, will modify file
def update_cover_letter(filename):
    doc = Document(filename)
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(11)
    oldtext = ""
    new_filename = get_company() + "_Cover_Letter.docx"
    for paragraph in doc.paragraphs:
        oldtext = paragraph.text
        if "_Date_" in paragraph.text:
            paragraph.text = oldtext.replace("_Date_", get_date(), 1)
            paragraph.style = doc.styles['Normal']
            doc.save(new_filename)

        if "_Company_" in paragraph.text:
            paragraph.text = oldtext.replace("_Company_", get_company(), 1)
            paragraph.style = doc.styles['Normal']
            doc.save(new_filename)

        if "_Position_" in paragraph.text:
            paragraph.text = oldtext.replace("_Position_", get_company(), 1)
            paragraph.style = doc.styles['Normal']
            doc.save(new_filename)

        if "_Recruiter_" in paragraph.text:
            paragraph.text = oldtext.replace("_Company_", get_company(), 1)
            paragraph.style = doc.styles['Normal']
            doc.save(new_filename)


def get_date():
    current_time = datetime.datetime.now()
    day = str(current_time.day)
    month = str(current_time.month)
    year = str(current_time.year)
    date = month + "/" + day + "/" + year
    return date


def get_company():
    pass


def get_recruiter():
    pass


def get_position():
    pass



