import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: EN or ES or FR")


@pytest.fixture(scope="function")
def browser(request):
    lang_name = request.config.getoption("language")
    browser = None
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang_name})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
