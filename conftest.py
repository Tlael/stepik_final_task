import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help='Select localisation language, e.g. en, es etc.')
    parser.addoption('--browser', action='store', default='chrome', help='Select browser, e.g. chrome, firefox')


@pytest.fixture(scope='function')
def browser(request):
    browser_option = request.config.getoption('--browser')
    language_option = request.config.getoption('--language')

    if browser_option == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language_option})
        browser = webdriver.Chrome(options=options)
    elif browser_option == 'firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', language_option)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('--browser should be chrome or firefox')

    yield browser

    browser.quit()
