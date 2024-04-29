from playwright.sync_api import Page, Locator


class EcoFriendlyLocators:
    product = '[class="item product product-item"]'
    size_option = '#option-label-size-143-item-172'
    color_option = '#option-label-color-93-item-49'
    input_qty = '#qty'
    add_to_cart = '#product-addtocart-button'
    shopping_cart = '#maincontent > div.page.messages > div:nth-child(2) > div > div > div > a'
    size = '#shopping-cart-table > tbody > tr.item-info > td.col.item > div > dl > dd:nth-child(2)'
    qty = '[class="input-text qty"]'
    delete_item = '[class="action action-delete"]'
    filter_size = '//*[@class="filter-options-title"]'
    actual_size = '[class="swatch-option text "]'
    filter_value = '[class="filter-value"]'
    clear_all = '#layered-filter-block > div.block-content.filter-content > div.block-actions.filter-actions > a > span'
    product_item = '[class="product-item-info"]'
    compare_button = '[class="action tocompare"]'
    product_name = '[class="product-item-name"]'
    first_name_product = '#compare-items > li > strong > a'
