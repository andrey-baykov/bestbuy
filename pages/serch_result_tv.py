from selenium.webdriver.common.by import By


class BestBuySearchResultTV:
    price = 0.0
    count = 0

    def __init__(self, browser):
        self.browser = browser

    def title(self):
        return self.browser.title

    def search(self, sku_id):
        self.browser.find_element(By.XPATH, "//button[@data-sku-id='" + sku_id + "']").click()

    def get_cart(self):
        self.browser.find_element(By.XPATH, "//a[@title='Cart']").click()

    def continue_shopping(self):
        self.browser.find_element(By.XPATH, "//button[text()='Continue shopping']").click()

    def get_item_price(self, sku_id):
        pass  # self.browser.find_element(By.XPATH, "//button[@data-sku-id='" + sku_id + "']")


"""        
        Find button
        find all prices and fill out it in the list
        return list
        maybe convert it first
"""
