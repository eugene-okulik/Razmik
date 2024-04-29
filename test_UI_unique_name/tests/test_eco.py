import pytest


@pytest.mark.smoke
def test_product(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.choose_item()
    eco_friendly.check_right_size("29")
    eco_friendly.check_right_qty('10')


@pytest.mark.regression
def test_filter(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.filter('XS')


@pytest.mark.regression
def test_compare_item(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.compare_product()
    eco_friendly.check_name_item()
