import time

import WebDriver
import Lookup

searchTerms = {
    "city": "Gainesville",
    "state": "Florida",
    "title": "Computer Engineering Intern"
}

print("CS-Search online!")
active = 1
while active:
    input_number = input("You will need to select your search type: \n 1: Preset \n")
    if input_number == '1':
        Lookup.lookup_jobs(searchTerms)
    elif input_number == '2':
        pass
    elif input_number == '4':
        active = 0
time.sleep(1)
WebDriver.driver.quit()
