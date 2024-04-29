import pytest
from playwright.sync_api import BrowserContext
from pages.create_account_page import CreateAccount
from pages.eco_friendly_page import EcoFriendly
from pages.sale_page import Sales


@pytest.fixture()
def page(context: BrowserContext, playwright):
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


@pytest.fixture()
def create_account(page):
    return CreateAccount(page)


@pytest.fixture()
def eco_friendly(page):
    return EcoFriendly(page)


@pytest.fixture()
def sales(page):
    return Sales(page)
