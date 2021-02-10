import time
import math
from selenium import webdriver

def ln(x):
    pass
def sin(x):
    pass

def calc(x):
    pass

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    browser.find_element_by_id("answer").send_keys(str(y))
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_css_selector("body > div > form > div > div > button").click()
finally:
    time.sleep(15)
    browser.quit()
