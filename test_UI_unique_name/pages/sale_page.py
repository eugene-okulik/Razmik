from pages.base_page import BasePage
from pages.locators.sale_locators import SaleLocators
from playwright.sync_api import expect


class Sales(BasePage):
    page_url = "sale.html"

    def choose_main_block(self):
        self.find(SaleLocators.main_promo).click()

    def choose_man_block(self):
        self.find(SaleLocators.sales_men).click()

    def choose_woman_block(self):
        self.find(SaleLocators.sales_women).click()

    def check_title(self, text):
        expect(self.find(SaleLocators.page_title)).to_have_text(text)
