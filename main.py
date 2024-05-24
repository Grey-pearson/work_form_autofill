# this will be to automate a form i must fill multiple times a day
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urls

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-data-dir={urls.CHROME_USER_DIR}")
chrome_options.add_argument("profile-directory=Default")

driver = webdriver.Chrome(options=chrome_options)
driver.get(urls.LINK)
