import time
from selenium.webdriver.common.by import By

def test_button_basket(browser):
    site = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    time.sleep(30)
    assert site, 'Not found'