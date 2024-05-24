# this will be to automate a form i must fill multiple times a day
from selenium import webdriver
from urls import link


driver = webdriver.Chrome()
driver.get(link)
