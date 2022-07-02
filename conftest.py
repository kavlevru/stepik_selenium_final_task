import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Добавление аргументов для запуска тестов
def pytest_addoption(parser):
    parser.addoption('--browser_name', default='chrome', action='store', help='choose browser firefox or chrome')
    parser.addoption('--language', default='en', action='store', help='Choose language for testing')


@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('language')
    if user_language is None:
        raise pytest.UsageError('--language must have the value es, fr, ru or other')
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name == 'chrome':
        # код определения языка для Chrome
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        # код определения языка для Firefox
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('--browser_name must have the value firefox or chrome')
    yield browser
    browser.quit()
