from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(10)
    yield chrome_driver


def test_submit(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    select = driver.find_element(By.ID, 'id_choose_language')
    dropdown = Select(select)
    dropdown.select_by_value('1')
    button_submit = driver.find_element(By.ID, 'submit-id-submit')
    button_submit.submit()
    result_text = driver.find_element(By.ID, 'result-text')
    print(result_text.text)


def test_start(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    button_start = driver.find_element(By.XPATH, '//*[@id="start"]/button')
    button_start.click()
    finish_result = driver.find_element(By.XPATH, '//*[@id="finish"]/h4')
    assert finish_result.text == 'Hello World!'
