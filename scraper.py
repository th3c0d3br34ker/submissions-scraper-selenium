from selenium import webdriver
from pathlib import Path
from time import sleep
from core.hr_scrapper import HR_Scrapper
import logging

from credentials import username, password
from tracks import TRACKS
from core.util import setupPath
from constants import WEBDRIVER_DIR

from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

setupPath()

logging.basicConfig(filename="logs.txt")
hr_scrap = HR_Scrapper()

chromedriver_path = Path(WEBDRIVER_DIR)
chrome_options = options.Options()
chrome_options.add_argument('--ignore-errors')

driver = webdriver.Chrome(
    executable_path=chromedriver_path,
    options=chrome_options
)
driver.get("https://www.hackerrank.com/auth/login")

driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)

sleep(5)

for i in TRACKS:
    try:
        hr_scrap.get_track(i, driver)
    except Exception as e:
        print("Something went wrong::", str(e))
        logging.warning(e)

driver.quit()
