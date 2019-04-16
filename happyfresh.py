from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()


def login():
    driver.get("https://www.happyfresh.co.th/gourmet-market-paragon/")
    driver.find_element_by_css_selector("css=.nav-signup-login > .arrow-down").click()
    driver.find_element_by_link_text("Log In").click()
    driver.find_element_by_id("login-email").send_keys()
    driver.find_element_by_id("login-password").send_keys()
    


if __name__ == "__main__":
    init()
    login()
    