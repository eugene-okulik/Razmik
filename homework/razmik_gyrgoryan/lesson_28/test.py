from playwright.sync_api import Page, expect, Request, Route
import json
import re


def test_iphone(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body["body"]["digitalMat"][0]["familyTypes"][0]["productName"] = "яблокофон 15 про"
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )
    page.route(re.compile('library/step0_iphone/digitalmat'), handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('[class="rf-hcard-content tile as-util-relatedlink"]').locator('nth=0').click()
    title = page.locator('[id="rf-digitalmat-overlay-label-0"]').locator('nth=0')
    expect(title).to_have_text('яблокофон 15 про')
