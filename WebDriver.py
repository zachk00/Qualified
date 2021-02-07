from selenium import webdriver
import config

#Main Init
print("Running CS-Search")
driver = webdriver.Firefox()
driver.get(config.url)