import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='es', help="Choose language of website")

@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("language")
    if lang == "es":
        link = "http://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207/"
    elif lang == "fr":
        link = "http://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207/"
    else:
        raise pytest.UsageError("You must select a supported language for this site")
    browser = webdriver.Chrome()
    browser.get(link)
    yield browser
    browser.quit()