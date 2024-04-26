from pages.base_page import BasePage
from pages.locators.create_account import CreateAccountLocators
from playwright.sync_api import expect


class CreateAccount(BasePage):
    page_url = "customer/account/create/"

    def login_form(self, first_name, second_name, email, passw, passw_confirmed):
        self.find(CreateAccountLocators.email).press_sequentially(email, delay=700)
        self.find(CreateAccountLocators.first_name).fill(first_name)
        self.find(CreateAccountLocators.second_name).fill(second_name)
        # self.find(CreateAccountLocators.email).fill(email)
        self.find(CreateAccountLocators.passw).fill(passw)
        self.find(CreateAccountLocators.passw_confirmed).fill(passw_confirmed)
        self.find(CreateAccountLocators.create_account).click()

    def check_right_text(self, text):
        right_text = self.find(CreateAccountLocators.success_text)
        expect(right_text).to_have_text(text)

    def check_correct_title(self, text):
        correct_title = self.find(CreateAccountLocators.title_wrapper)
        expect(correct_title).to_have_text(text)

    def check_is_error_account(self, text):
        text_error = self.find(CreateAccountLocators.error_message)
        expect(text_error).to_have_text(text)

    def incorrect_email(self, text):
        error_email = self.find(CreateAccountLocators.email_error)
        expect(error_email).to_have_text(text)
