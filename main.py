from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from urls import LINK
from Class.CamConfig import BrowserControl


browser_control = BrowserControl()

browser_control.sign_in()

# browser_control.close()
