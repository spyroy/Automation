from selenium import webdriver
from selenium.webdriver.common.by import By


def test_google_search():
    driver = webdriver.Chrome()
    driver.get('https://google.com')
    driver.find_element(By.NAME, 'q').send_keys('puppies')
    driver.find_element(By.NAME, 'btnK').submit()
    assert 'puppies' in driver.title


