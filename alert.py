import time
import math
from selenium import webdriver


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("body > form > div > div > button").click()
    alert = browser.switch_to.alert
    alert.accept()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    browser.find_element_by_css_selector("body > form > div > div > button").click()
finally:
    time.sleep(15)
    browser.quit()
