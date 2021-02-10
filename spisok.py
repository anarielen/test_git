import time
from selenium import webdriver
from selenium.webdriver.support.select import Select


def z(args):
    pass


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("num1")
    y = browser.find_element_by_id("num2")

    def calc(z):
        return str(int(x) + int(y))
    z = calc(z)

    select = Select(browser.find_element_by_tag_name("custom-select"))
    select.select_by_value(z)

    button = browser.find_element_by_css_selector("button.btn").click()
finally:
    time.sleep(5)
    browser.quit()
