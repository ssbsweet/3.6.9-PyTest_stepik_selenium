import pytest   # импорт пайтест
from selenium import webdriver  # импорт вебдрайвера
from selenium.webdriver.chrome.options import Options   # импорт Options

def pytest_addoption(parser):   #   парсер
    parser.addoption('--language', action='store', default=None,    #--язык, действие - собрать, по-умолчанию - ничего, хелп
                     help="Choose browser: chrome")


@pytest.fixture(scope="function")   # область приминения
def browser(request):  # переменная задаем
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()


