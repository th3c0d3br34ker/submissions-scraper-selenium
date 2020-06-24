from selenium import webdriver


def setupSeleniumDriver() -> webdriver:
    from core.constants import WEBDRIVER_DIR
    from selenium.webdriver.chrome import options

    chromedriver_path = WEBDRIVER_DIR
    chrome_options = options.Options()
    chrome_options.add_argument("--ignore-errors")
    chrome_options.add_argument("--log-level=OFF")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(
        executable_path=chromedriver_path,
        options=chrome_options
    )
    return driver
