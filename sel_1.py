from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "price"), "100")
        )

    browser.find_element(By.ID, "book").click()

    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text

    result = calc(x)

    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(result)

    browser.find_element(By.CSS_SELECTOR, '#solve').click()

finally:
    time.sleep(10)
    browser.quit()
