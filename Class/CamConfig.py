from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoSuchElementException, ElementNotInteractableException
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

        # all the shtuff needed to get
        # self.driver.implicitly_wait(3)
        errors = [NoSuchElementException, ElementNotInteractableException]

        wait = WebDriverWait(
            self.driver, timeout=5, poll_frequency=0.2, ignored_exceptions=errors
        )
        wait.until(lambda d: log_in_button.send_keys("Displayed") or True)
        log_in_button = self.driver.element(
            By.XPATH,
            "/html/body/div[2]/div[2]/main/div[2]/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div[2]/a",
        )

        WebDriverWait(driver, 100, poll_frequency=0.1).until(
            EC.element_to_be_clickable(By.ID, "search_button")
        ).click()

        log_in_button.click()

    # works
    def open_service_now(self):
        self.driver.implicitly_wait(10)
        service_now_button = self.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/section/main/div/section/section/section[2]/section/div/section/div[29]/a/article",
        )
        service_now_button.click()

    # needs sign in help as well or to be a brand new tab to keep SSO working
    def open_old_vms(self):
        self.driver.get(OLD_VMS)

    def close(self):
        self.driver.close()
