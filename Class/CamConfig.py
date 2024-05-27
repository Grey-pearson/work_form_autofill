from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from urls import LINK

# this will open browser,
# log into okta > service now
# fill and submit form
# funcs to close chorme at the end ig?


class CamConfig:
    def __init__(self):
        self.running = False
        # idk what else to put here
