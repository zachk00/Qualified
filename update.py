from docx import Document
from docx.shared import Pt
import datetime
import JobCard
import csv


# only pass a copy of the file, will modify file
def update_cover_letter(jobcard):
    company = jobcard.employer
    position = jobcard.title

    location = jobcard.location

    doc = Document("Documents/Cover_Letter.docx")
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(11)
    oldtext = ""
    new_filename = company + "_Cover_Letter.docx"
    for paragraph in doc.paragraphs:
        oldtext = paragraph.text
        if "_Date_" in paragraph.text:
            paragraph.text = oldtext.replace("_Date_", get_date(), 1)
            paragraph.style = doc.styles['Normal']
            doc.save(new_filename)

        if "_Company_" in paragraph.text:
            paragraph.text = oldtext.replace("_Company_", company, 1)
            paragraph.style = doc.styles['Normal']
            doc.save(new_filename)

        if "_Title_" in paragraph.text:
            paragraph.text = oldtext.replace("_Title_", position, 1)
            paragraph.style = doc.styles['Normal']
            doc.save(new_filename)

        if "_Location_" in paragraph.text:
            paragraph.text = oldtext.replace("_Location_", location, 1)
            paragraph.style = doc.styles['Normal']
            doc.save(new_filename)


def get_date():
    current_time = datetime.datetime.now()
    day = str(current_time.day)
    month = str(current_time.month)
    year = str(current_time.year)
    date = month + "/" + day + "/" + year
    return date


def write_listing(jobcards):
    fields = ['title', 'employer', 'salary', 'location', 'qualification', 'link']

    rows = []
    temp = []
    for job in jobcards:
        temp.append(job.title)
        temp.append(job.employer)
        temp.append(job.salary)
        temp.append(job.location)
        temp.append(job.link)

        rows.append(temp)


    with open("Documents/Qualified_Jobs.csv", 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)

        # writing the data rows
        csvwriter.writerows(rows)
