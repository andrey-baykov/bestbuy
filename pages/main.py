from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BestBuy:
    URL = "https://www.bestbuy.com/"
    SEARCH = (By.XPATH, "//input[@id='gh-search-input']")
    SEARCH_BUTTON = (By.XPATH, "//button[@title='submit search']")

    def __init__(self, browser):
        self.browser = browser

    def load(self, url=""):
        self.browser.get(self.URL + url)

    def search(self, text_to_search):
        self.browser.find_element(*self.SEARCH).send_keys(text_to_search)
        self.browser.find_element(*self.SEARCH_BUTTON).click()

    def title(self):
        return self.browser.title
