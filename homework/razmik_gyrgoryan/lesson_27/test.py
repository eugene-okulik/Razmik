from playwright.sync_api import Page, expect, BrowserContext, Dialog


def test_alert(page: Page):
    page.on('dialog', lambda alert: alert.accept())
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.locator('#content > a.a-button').click()
    you_selected = page.locator('#result-text')
    expect(you_selected).to_have_text('Ok')


def test_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    button = page.locator('#new-page-button')
    with context.expect_page() as new_page_event:
        button.click()
    new_page = new_page_event.value
    result = new_page.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    new_page.close()
    expect(button).to_be_enabled()


def test_visible_complete(page: Page):
    page.goto('https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html')
    button = page.locator('#downloadButton')
    button.click()
    button_unvisible = page.locator('#dialog > div.progress-label')
    expect(button_unvisible).to_be_visible()
    close = page.get_by_text('Close')
    close.click()
