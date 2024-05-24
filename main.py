# this will be to automate a form i must fill multiple times a day
from selenium import webdriver
from urls import link

# keep brower open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(link)
