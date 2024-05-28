from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from urls import LINK
from Class.CamConfig import BrowserControl


def click_service_now():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(LINK)
    driver.find_element(By.LINK_TEXT, value="select")
    driver.implicitly_wait(60)
    # click on img name ServiceNow logo
    service_now = driver.find_element(By.LINK_TEXT, value="ServiceNow")
    # driver.find_element(By.NAME, "revealed")

    wait = WebDriverWait(driver, timeout=60)
    wait.until(lambda d: service_now.is_displayed())

    print(service_now)
    # click on button name rquest catolog
    # find element to select for config request
    # fill out form

    # im going to create tkinter ui for this as well probably


# click_service_now()

browser_control = BrowserControl()

browser_control.sign_in()

# browser_control.close()
