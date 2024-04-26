import pytest
from utils.faker import generate_email, generate_password, generate_name


@pytest.mark.smoke
def test_correct_form(create_account):
    create_account.open_page()
    email = generate_email()
    password = generate_password()
    name = generate_name()
    create_account.login_form(name, name, email, password, password)
    create_account.check_right_text('Thank you for registering with Main Website Store.')
    create_account.check_correct_title('My Account')


@pytest.mark.regression
def test_error_account(create_account):
    create_account.open_page()
    password = generate_password()
    name = generate_name()
    create_account.login_form(name, name, 'test@gmail.com', password, password)
    create_account.check_is_error_account(
        "There is already an account with this email address. "
        "If you are sure that it is your email address, click here to get your password and access your account."
    )


@pytest.mark.regression
def test_incorrect_email(create_account):
    create_account.open_page()
    password = generate_password()
    name = generate_name()
    create_account.login_form(name, name, 'test', password, password)
    create_account.incorrect_email("Please enter a valid email address (Ex: johndoe@domain.com).")
