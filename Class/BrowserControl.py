from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from urls import LINK, OLD_VMS

# this will open browser,
# log into okta > service now
# fill and submit form
# funcs to close chorme at the end ig?


class BrowserControl:
    def __init__(self):
        # set up function to create driver ig?
        chrome_options = webdriver.ChromeOptions()
        chrome_options.page_load_strategy = "normal"
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)

    def sign_in(self):
        self.driver.get(LINK)

        WebDriverWait(self.driver, 100, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body/div[2]/div[2]/main/div[2]/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div[2]/a",
                )
            )
        ).click()

        print("sign_in success")

    # works
    def open_service_now(self):

        WebDriverWait(self.driver, 100, poll_frequency=0.1).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body/div[2]/div/div/section/main/div/section/section/section[2]/section/div/section/div[29]/a/article",
                )
            )
        ).click()
        print("open_service_now success")

    # needs sign in help as well or to be a brand new tab to keep SSO working
    def open_old_vms(self):
        self.driver.switch_to.new_window("tab")
        self.driver.get(OLD_VMS)
        #  sign in somehow ig
        print("open_old_service_now success")

    def close(self):
        self.driver.close()
        print("close success")
