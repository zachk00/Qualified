from selenium import webdriver
import JobCard

# Initialization
url = "https://www.indeed.com/"
driver = webdriver.Firefox()
driver.implicitly_wait(5)


def lookup_jobs(searchTerms):
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
        jobList = [""]
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
    else:
        print("Unable to load listings.")

    return jobList
