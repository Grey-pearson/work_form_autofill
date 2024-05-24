# this will be to automate a form i must fill multiple times a day
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urls

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_options.add_argument(f"user-data-dir={urls.CHROME_USER_DIR}")
# setting chrome driver path
driver = webdriver.Chrome(executable_path)
