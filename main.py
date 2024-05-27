from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import selenium.webdriver.support.ui as ui
from urls import LINK


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(LINK)


# click on img name ServiceNow logo
service_now = driver.find_element(by="name", value="ServiceNow logo")
wait = ui.WebDriverWait(driver=driver, timeout=30)
wait.until(lambda d: service_now.is_displayed)
print(service_now)
# click on button name rquest catolog
# find element to select for config request
# fill out form

# im going to create tkinter ui for this as well probably
driver.close()
