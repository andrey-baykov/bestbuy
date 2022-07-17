from pages.main import BestBuy
from pages.serch_result_tv import BestBuySearchResultTV
from pages.cart import Cart
import json
import time
from selenium.webdriver.common.by import By

with open("../data.json", "r") as file:
    data = json.load(file)


def test_add_goods(browser):
    prices = {'original_price': '$1,069.98', 'savings': '-$90.00', 'store_pickup': 'Free', 'sales_tax': '$75.95',
              'recycling_fee': '$6.00', 'total': '$1,061.93'}
    start_page = BestBuy(browser)
    result_page = BestBuySearchResultTV(browser)
    cart_page = Cart(browser)
    count_items_to_test = len(data["items"])
    for item in range(0, count_items_to_test):
        test_item = data["items"][item]
        start_page.load("")
        assert start_page.title() == "Best Buy | Official Online Store | Shop Now & Save"
        start_page.search(test_item[1])
        result_page.search(test_item[0])
        # run function to bring prices and add it to the prices_dict
    result_page.get_cart()
    cart_page.check_price(prices)
    time.sleep(3)
