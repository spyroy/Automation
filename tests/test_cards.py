import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from royale.pages.card_details_page import CardDetailsPage
from royale.pages.cards_page import CardsPage


def test_ice_spirit_card():
    c = DesiredCapabilities.CHROME
    c["pageLoadStrategy"] = "none"
    driver = webdriver.Chrome(desired_capabilities=c)
    wait = WebDriverWait(driver, 20)
    driver.get('https://statsroyale.com')
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class='header__slideNavIcon']")))
    # driver.find_element(By.NAME("body")).send_keys("Keys.ESCAPE")
    # driver.execute_script("window.stop()")
    # driver.find_element(By.NAME("body")).send_keys("Keys.ESCAPE")
    # driver.set_window_size(1024, 600)
    driver.maximize_window()
    # time.sleep(10)
    # driver.execute_script("window.scrollTo(0,900)")
    # time.sleep(1)
    # driver.find_element(By.CSS_SELECTOR, "[class='header__slideNavIcon']").click()
    # time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[href*='Ice+Spirit']")))
    # driver.execute_script("window.stop()")
    ice_spirit_card = driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']")
    driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']").click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class*='cardName']")))
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class*='card__common']")))
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class*='card__rarity']")))
    card_name = driver.find_element(By.CSS_SELECTOR, "[class*='cardName']").text
    card_common = driver.find_element(By.CSS_SELECTOR, "[class*='card__common']").text
    card_rarity = driver.find_element(By.CSS_SELECTOR, "[class*='card__rarity']").text
    index = card_rarity.find(',')
    card_arena = card_rarity[index + 2:]
    card_type = card_rarity[0:index]

    # driver.execute_script("window.stop()")
    assert ice_spirit_card.is_displayed
    assert card_name == 'Ice Spirit'
    assert card_common == 'Common'
    assert card_arena == 'Arena 8'
    assert card_type == 'Troop'


def test_ice_golem_card_is_displayed():
    c = DesiredCapabilities.CHROME
    c["pageLoadStrategy"] = "none"
    driver = webdriver.Chrome(desired_capabilities=c)
    wait = WebDriverWait(driver, 20)
    driver.get('https://statsroyale.com')
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class='header__slideNavIcon']")))
    # driver.find_element(By.NAME("body")).send_keys("Keys.ESCAPE")
    # driver.execute_script("window.stop()")
    # driver.find_element(By.NAME("body")).send_keys("Keys.ESCAPE")
    # driver.set_window_size(1024, 600)
    driver.maximize_window()
    # time.sleep(10)
    # driver.execute_script("window.scrollTo(0,900)")
    # time.sleep(1)
    # driver.find_element(By.CSS_SELECTOR, "[class='header__slideNavIcon']").click()
    # time.sleep(5)
    # driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()
    cards_page = CardsPage(driver).goto()
    ice_golem = cards_page.get_card_by_name('Ice Golem')
    assert ice_golem.is_displayed()


def test_ice_golem_details_displayed():
    c = DesiredCapabilities.CHROME
    c["pageLoadStrategy"] = "none"
    driver = webdriver.Chrome(desired_capabilities=c)
    wait = WebDriverWait(driver, 20)
    driver.get('https://statsroyale.com')
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class='header__slideNavIcon']")))
    driver.maximize_window()
    CardsPage(driver).goto().get_card_by_name('Ice Golem').click()
    details_page = CardDetailsPage(driver)
    card_name = details_page.map.card_name.text
    split = details_page.map.card_category.text.split(', ')
    card_type = split[0]
    card_arena = split[1]
    card_rarity = details_page.map.card_rarity.text.split('\n')[1]

    assert card_name == 'Ice Golem'
    assert card_type == 'Troop'
    assert card_arena == 'Arena 8'
    assert card_rarity == 'Rare'
