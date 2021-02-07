from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time

import WebDriver
import config

# Initialization
url = "https://www.indeed.com/"
WebDriver.driver.implicitly_wait(10)


def lookup_jobs(searchTerms):
    new_url = url + "jobs?q={}&l={}%2C+{}".format(searchTerms["title"], searchTerms["city"], searchTerms["state"])
    WebDriver.driver.get(new_url)
    page = 1
    totalJobs = 0
    print("Checking Page " + str(page) + " of " + searchTerms["title"] + " positions.")

    locations = []
    # Check different websites

    # Indeed
    if WebDriver.driver.find_element_by_xpath(
            "//*[@class='jobsearch-SerpJobCard unifiedRow row result clickcard']"):
        listings = WebDriver.driver.find_elements_by_xpath(
            "//*[@class='jobsearch-SerpJobCard unifiedRow row result clickcard']")
        totalJobs = len(listings)
        for job in listings:
            selectTitle = job.find_element_by_xpath("//*[@class='jobsearch")
            title = selectTitle.get_attribute("value")

            selectCompany = job.find_element_by_class_name("company")
            company = selectCompany.get_attribute("value")

            #selectLocation = job.find_element_by_class_name("location accessible-contrast-color-location")
            #location = selectTitle.get_attribute("value")

            print(title)

    else:
        print("Unable to load listings.")
