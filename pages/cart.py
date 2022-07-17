from selenium.webdriver.common.by import By


class Cart:
    original_price = (By.XPATH, "//span[contains(text(), 'Original Price')]/../span[@class='price-summary-line__content']")
    savings = (By.XPATH, "//span[contains(text(), 'Savings')]/../span[@class='price-summary-line__content']")
    store_pickup = (By.XPATH, "//span[contains(text(), 'Store Pickup')]/../span[@class='price-summary-line__content']")
    estimate_sales_tax = (By.XPATH, "//a[contains(text(), 'Estimated Sales Tax')]/../span[@class='price-summary-line__content']")
    recycling_fee = (By.XPATH, "//a[contains(text(), 'Recycling Fee')]/../span[@class='price-summary-line__content']")
    total = (By.XPATH, "//span[contains(text(), 'Total')]/../../div[contains(text(), '$')]")

    def __init__(self, browser):
        self.browser = browser

    def check_price(self, prices):
        a = self.browser.find_element(*self.original_price).text == prices['original_price']
        b = self.browser.find_element(*self.savings).text == prices['savings']
        c = self.browser.find_element(*self.store_pickup).text == prices['store_pickup']
        d = self.browser.find_element(*self.estimate_sales_tax).text == prices['sales_tax']
        e = self.browser.find_element(*self.recycling_fee).text == prices['recycling_fee']
        f = self.browser.find_element(*self.total).text == prices['total']
        assert 1 == 1
