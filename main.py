from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from urls import LINK
from Class.BrowserControl import BrowserControl


browser_control = BrowserControl()

browser_control.sign_in()

browser_control.open_service_now()

browser_control.open_old_vms()

# browser_control.close()
