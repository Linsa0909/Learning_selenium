import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


def test_eight_components():
    driver = setup()
    title = driver.title
    assert title == "Web form"
    driver.implicitly_wait(3)
    test_box = driver.find_element(by=By.NAME, value = 'my-text')
    submit_button = driver.find_element(by=By.CSS_SELECTOR,value='button')

    test_box.send_keys("Selenium")
    submit_button.click()
    time.sleep(3)
    message = driver.find_element(by=By.ID, value = "message")
    value = message.text
    assert value == "Received!"
    time.sleep(5)
    teardown(driver)

def setup():
    # 使用 GeckoDriverManager 自动下载并设置 GeckoDriver 路径
    service = Service(GeckoDriverManager().install())
    # 创建firefox浏览器驱动实例
    driver = webdriver.Firefox(service=service)

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    return driver

def teardown(driver):
    driver.quit()