from playwright.sync_api import Playwright, Page, Route
from data_json import *

co2_counter = '//*[@class="desktop-impact-item-eeQO3"][2]'
water_counter = '//*[@class="desktop-impact-item-eeQO3"][4]'
energy_counter = '//*[@class="desktop-impact-item-eeQO3"][6]'
all_counters = "//div[contains(@class,'desktop-impact-items')]"

main_url = "https://www.avito.ru/avito-care/eco-impact"
rout_url = "https://www.avito.ru/web/1/charity/ecoImpact/init"


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(main_url)

    page.locator(co2_counter).screenshot(path='./output/tс01-CO2.png')
    page.locator(water_counter).screenshot(path='./output/tс01-water.png')
    page.locator(energy_counter).screenshot(path='./output/tс01-energy.png')
    page.locator(all_counters).screenshot(path='./output/tс01-all_counters.png')
    context.close()
    browser.close()


def test_counter_1(page: Page):
    def handle(route: Route):
        json = thousand_boundary_below_json
        route.fulfill(json=json)

    page.route(rout_url, handle)

    page.goto(main_url)

    page.wait_for_selector('div[class^="desktop-impact-items"]')

    waterCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0:
            waterCounter = elem

    assert waterCounter != None

    waterCounter.screenshot(path="output/TC-02.png")

    page.wait_for_timeout(5000)


def test_counter_2(page: Page):
    def handle(route: Route):
        json = thousand_boundary_json
        route.fulfill(json=json)

    page.route(rout_url, handle)

    page.goto(main_url)

    page.wait_for_selector('div[class^="desktop-impact-items"]')

    waterCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0:
            waterCounter = elem

    assert waterCounter != None

    waterCounter.screenshot(path="output/TC-03.png")

    page.wait_for_timeout(5000)


def test_counter_3(page: Page):
    def handle(route: Route):
        json = thousand_boundary_above_json
        route.fulfill(json=json)

    page.route(rout_url, handle)

    page.goto(main_url)

    page.wait_for_selector('div[class^="desktop-impact-items"]')

    waterCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0:
            waterCounter = elem

    assert waterCounter != None

    waterCounter.screenshot(path="output/TC-04.png")

    page.wait_for_timeout(5000)


def test_counter_4(page: Page):
    def handle(route: Route):
        json = minus_one_json
        route.fulfill(json=json)

    page.route(rout_url, handle)

    page.goto(main_url)

    page.wait_for_selector('div[class^="desktop-impact-items"]')

    waterCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0:
            waterCounter = elem

    assert waterCounter != None

    waterCounter.screenshot(path="output/TC-05.png")

    page.wait_for_timeout(5000)
