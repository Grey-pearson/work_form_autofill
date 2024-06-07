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
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.page_load_strategy = "normal"
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

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

    # def
    # request catelog
    # "/html/body/macroponent-f51912f4c700201072b211d4d8c26010//div/sn-canvas-appshell-root/sn-canvas-appshell-layout/sn-polaris-layout/div/sn-canvas-appshell-main//div/sn-canvas-experience-shell/macroponent-76a83a645b122010b913030a1d81c780//div/sn-canvas-root/sn-canvas-layout/sn-canvas-main//main/sn-canvas-screen//section/screen-action-transformer-b1fb5f821b6e611086baed71604bcb84/macroponent-b5fb5f821b6e611086baed71604bcb80//div/now-uxf-page/div/now-uxf-page-simple-container/div/now-uxf-page-simple-container[2]/div/now-uxf-page-simple-container[2]/div/now-uxf-page-simple-container/div/now-button-bare[1]//button"
    # reconfiguration request
    # "/html/body/div/section/main/div[3]/div/sp-page-row/div/div[1]/span[1]/div/div/div[2]/div[1]/div[2]/div/div/div/div/a"
    # click to get to where tdc gets entered
    # "/html/body/div[1]/section/main/div[2]/div/sp-page-row/div/div/span[1]/div/div/div/div/div[1]/div[1]/div/div[2]/form/div/sp-variable-layout/div[1]/div/div/div[3]/div/span/span/div/div/a"
    # where tdc goes in form
    # "/html/body/div[3]/div/input"

    # needs sign in help as well or to be a brand new tab to keep SSO working
    def open_old_vms(self):
        self.driver.switch_to.new_window("tab")
        self.driver.get(OLD_VMS)
        #  sign in somehow ig
        print("open_old_service_now success")

    def close(self):
        self.driver.close()
        print("close success")
