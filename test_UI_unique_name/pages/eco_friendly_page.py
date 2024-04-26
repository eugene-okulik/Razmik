from pages.base_page import BasePage
from pages.locators.eco_friendly import EcoFriendlyLocators
from playwright.sync_api import expect


class EcoFriendly(BasePage):
    page_url = "collections/eco-friendly.html"
    value = None
    text_actual_size = None
    actual_size = None
    qty_text = None
    qty = None
    text_size = None
    size = None

    def choose_item(self):
        self.find(EcoFriendlyLocators.product).locator('nth=0').click()
        self.size = self.find(EcoFriendlyLocators.size_option)
        self.text_size = self.find(EcoFriendlyLocators.size_option)
        self.size.click()
        self.find(EcoFriendlyLocators.color_option).click()
        self.qty = self.find(EcoFriendlyLocators.input_qty)
        self.qty_text = self.find(EcoFriendlyLocators.input_qty)
        self.qty.clear()
        self.qty.fill("10")
        self.find(EcoFriendlyLocators.add_to_cart).click()
        self.find(EcoFriendlyLocators.shopping_cart).click()

    def check_right_size(self, text):
        expect(self.find(EcoFriendlyLocators.size)).to_have_text(text)

    def check_right_qty(self, text):
        expect(self.find(EcoFriendlyLocators.qty)).to_have_value(text)

    def filter(self, text):
        self.find(EcoFriendlyLocators.filter_size).locator('nth=3').click()
        self.actual_size = self.find(EcoFriendlyLocators.actual_size).locator('nth=0')
        self.actual_size.click()
        self.value = self.find(EcoFriendlyLocators.filter_value)
        expect(self.value).to_have_text(text)
        self.find(EcoFriendlyLocators.clear_all).click()

    def compare_product(self):
        self.find(EcoFriendlyLocators.product_item).locator('nth=0').hover()
        self.find(EcoFriendlyLocators.compare_button).locator('nth=0').click()

    def check_name_item(self):
        text = self.find(EcoFriendlyLocators.first_name_product).inner_text()
        expect(self.find(EcoFriendlyLocators.product_name).locator('nth=1')).to_have_text(text)
