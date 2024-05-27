from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from urls import LINK


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(LINK)


# im going to create tkinter ui for this as well probably
