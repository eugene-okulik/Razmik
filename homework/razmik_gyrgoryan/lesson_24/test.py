import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(7)
    yield chrome_driver


def test_korzina(driver):
    driver.get('https://www.demoblaze.com/index.html')
    phone = driver.find_element(By.LINK_TEXT, 'Samsung galaxy s6')
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).click(phone).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    driver.find_element(By.LINK_TEXT, 'Add to cart').click()
    wait = WebDriverWait(driver, 10)
    alert = Alert(driver)
    wait.until(EC.alert_is_present())
    alert.accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    cart = driver.find_element(By.ID, 'cartur')
    cart.click()
    chosen_item = driver.find_element(By.CSS_SELECTOR, '#tbodyid > tr > td:nth-child(2)')
    assert chosen_item.text == 'Samsung galaxy s6'


def test_compare_product(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    product_item = driver.find_element(By.CSS_SELECTOR, '[class="product-item-info"]')
    action = ActionChains(driver)
    action.move_to_element(product_item)
    compare_button = driver.find_element(By.CSS_SELECTOR, '[class="action tocompare"]')
    action.click(compare_button)
    action.perform()
    product_name = driver.find_element(By.CSS_SELECTOR, '[class="product-item-name"]')
    first_name_product = driver.find_element(By.LINK_TEXT, 'Push It Messenger Bag')
    assert product_name.text == first_name_product.text
