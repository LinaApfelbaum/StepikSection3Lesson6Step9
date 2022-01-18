import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_multilingual_cart_button_exists(browser, pause):
    browser.get(link)
    time.sleep(pause)
    add_to_basket_button = browser.find_element(
        By.CLASS_NAME, "btn-add-to-basket")

    assert add_to_basket_button.tag_name == "button", "Element should have button tag"
