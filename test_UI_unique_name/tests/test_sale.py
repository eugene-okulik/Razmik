import pytest


@pytest.mark.regression
def test_main_block(sales):
    sales.open_page()
    sales.choose_main_block()
    sales.check_title('Women Sale')


@pytest.mark.regression
def test_man(sales):
    sales.open_page()
    sales.choose_man_block()
    sales.check_title('Men Sale')


@pytest.mark.regression
def test_woman(sales):
    sales.open_page()
    sales.choose_woman_block()
    sales.check_title('Gear')
