from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(5)
    yield chrome_driver


def test_submit(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    submit_field = driver.find_element(By.CSS_SELECTOR, '[name="text_string"]')
    submit_field.send_keys('Test')
    submit_field.submit()
    text_from_field = driver.find_element(By.ID, 'result-text')
    print(text_from_field.text)
