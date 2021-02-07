from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time
import JobCard
import config

# Initialization

url = "https://www.indeed.com/"


def lookup_jobs(searchTerms):
    PATH = "Resources/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(10)
    new_url = url + "jobs?q={}&l={}%2C+{}".format(searchTerms["title"], searchTerms["city"], searchTerms["state"])
    driver.get(new_url)
    page = 1
    totalJobs = 0
    print("Checking Page " + str(page) + " of " + searchTerms["title"] + " positions.")

    locations = []
    # Check different websites

    # Indeed
    recruiter = "Indeed"
    if driver.find_element_by_xpath(
            "//*[@class='jobsearch-SerpJobCard unifiedRow row result clickcard']"):
        listings = driver.find_elements_by_xpath(
            "//*[@class='jobsearch-SerpJobCard unifiedRow row result clickcard']")
        totalJobs = len(listings)
        jobList = []
        num_jobs = 0
        for job in listings:
            myJob = JobCard

            job.click()

            title = job.find_element_by_class_name("title").text
            try:
                if title.endswith('\nnew'):
                    title = title[:-4]
            except:
                pass
            myJob.title = title

            employer = job.find_element_by_class_name("company").text
            myJob.employer = employer

            try:
                location = job.find_element_by_class_name("location").text
            except:
                location = "Unknown"
            myJob.location = location

            try:
                salary = job.find_element_by_class_name("salaryText").text
            except:
                salary = "Unlisted"
            myJob.salary = salary

            link = driver.current_url
            myJob.link = link

            try:
                description = driver.find_element_by_xpath("//*[@class='jobsearch-jobDescriptionText']")
            except:
                description = "Not Found"
            myJob.description = description

            jobList.append(myJob)
            num_jobs += 1
            if num_jobs == 1:
                break

    else:
        print("Unable to load listings.")

    return jobList