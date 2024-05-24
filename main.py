# this will be to automate a form i must fill multiple times a day
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urls

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# chrome_options.add_argument(f"user-data-dir={urls.CHROME_USER_DIR}")
chrome_options.add_argument("profile-directory=Default")
chrome_driver = "C:\chromedriver.exe"

driver = webdriver.Chrome(options=chrome_options)
print(driver.title)
