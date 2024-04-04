import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from random import randint
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(7)
    yield chrome_driver


def test_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    first_name = driver.find_element(By.ID, 'firstName')
    first_name.send_keys('Test')
    second_name = driver.find_element(By.ID, 'lastName')
    second_name.send_keys('Test')
    email = driver.find_element(By.ID, 'userEmail')
    email.send_keys('test@gmail.com')
    gender = driver.find_element(By.CSS_SELECTOR, f"label[for='gender-radio-{randint(1, 3)}']")
    gender.click()
    number = driver.find_element(By.ID, 'userNumber')
    number.send_keys(123456789000)
    subjects = driver.find_element(By.CSS_SELECTOR, '#subjectsInput')
    subjects.send_keys('English')
    subjects.send_keys(Keys.ENTER)
    hobbies = driver.find_element(By.CSS_SELECTOR, f'label[for="hobbies-checkbox-{randint(1, 3)}"]')
    hobbies.click()
    address = driver.find_element(By.CSS_SELECTOR, '[placeholder="Current Address"]')
    address.send_keys('Test')
    select_one = driver.find_element(By.ID, 'react-select-3-input')
    select_one.send_keys('NCR')
    select_one.send_keys(Keys.ENTER)
    select_two = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'react-select-4-input')))
    select_two.send_keys('Delhi')
    select_two.send_keys(Keys.ENTER)
    button_submit = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#submit')))
    button_submit.click()
    table = driver.find_element(By.CSS_SELECTOR, '[class="table table-dark table-striped table-bordered table-hover"]')
    print(table.text)
