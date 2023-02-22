import pytest
from selene import be, have
from selene.support.shared import browser


@pytest.fixture
def browser_settings():
    browser.config.browser_name = 'firefox'
    browser.config.window_width = 720
    browser.config.window_height = 960

def test_google_search_positive(browser_settings):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('Selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_search_negative(browser_settings):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('89912313132121393030303039393').press_enter()
    browser.element('.card-section').should(have.text('По запросу 89912313132121393030303039393 ничего не найдено.'))