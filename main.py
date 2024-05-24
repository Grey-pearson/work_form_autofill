# this will be to automate a form i must fill multiple times a day
from selenium import webdriver
from urls import LINK, CHROME_USER_DIR

options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={CHROME_USER_DIR}")
options.add_argument("profile-directory=Default")

driver = webdriver.Chrome(options=options)
driver.get(LINK)
