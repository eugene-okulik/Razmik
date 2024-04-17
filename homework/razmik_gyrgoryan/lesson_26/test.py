import random
import time

from playwright.sync_api import Page, expect
import pytest


def test_login(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='username').fill('test')
    page.get_by_role('textbox', name='password').fill('test')
    page.get_by_role('button').click()


def test_submit(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.get_by_placeholder('First Name').fill('Test')
    page.get_by_placeholder('Last Name').fill('Test')
    page.get_by_placeholder('name@example.com').fill('test@gmail.com')
    page.locator(f'#gender-radio-{random.randint(1, 3)}').click()
    page.get_by_placeholder('Mobile Number').fill("1234567890")
    page.locator('#subjectsInput').fill('English')
    page.locator(f'#hobbies-checkbox-{random.randint(1, 3)}').click()
    page.get_by_placeholder('Current Address').fill("Test")
    page.locator('#react-select-3-input').fill('NCR')
    page.locator('#react-select-4-input').fill('Delhi')
    page.get_by_role('button', name="Submit").click()
