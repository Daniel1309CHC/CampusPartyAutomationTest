import pytest
from setup_driver import get_driver

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Navegador a usar: chrome, firefox o edge"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Ejecutar en modo headless"
    )

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver = get_driver(browser, headless)
    yield driver
    driver.quit()