from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

import configparser

driver = webdriver.Firefox()
username = ""
password = ""

product_url = {}
product_url["tomato"] = "https://www.happyfresh.co.th/gourmet-market-paragon/products/natural-and-premium-food-organic-tomato-114863/"
product_url["egg"] = "https://www.happyfresh.co.th/gourmet-market-paragon/products/natural-and-premium-food-organic-egg-10-pcs-158746/"


def init():
    global username
    global password
    config = configparser.ConfigParser()
    config.read('config.ini')
    username = config["credentials"]["username"]
    password = config["credentials"]["password"]


def login():
    driver.get("https://www.happyfresh.co.th/gourmet-market-paragon/")
    WebDriverWait(driver, 15).until(lambda x: x.find_element_by_css_selector(".nav-signup-login > .arrow-down"))
    driver.find_element_by_css_selector(".nav-signup-login > .arrow-down").click()
    driver.find_element_by_link_text("Log In").click()
    print(username)
    driver.find_element_by_id("login-email").send_keys(username)
    driver.find_element_by_id("login-password").send_keys(password)
    driver.find_element_by_css_selector("form > button:nth-child(3)").click()

def buystuff():

    while True:
        s = input('--> ')
        (product,quantity) = s.split()
        add_to_cart(product,quantity)
        if s == "done":
            break

def add_to_cart(product, quantity):

    if product not in product_url:
        print("Invalid Product or Quantity, please use format: product quantity")
        return

    open_and_add_product(product, quantity)

def open_and_add_product(product, quantity):
    driver.get(product_url[product])
    WebDriverWait(driver, 15).until(lambda x: x.find_element_by_css_selector(".numbers"))
    driver.find_element_by_css_selector(".numbers .ic-number").clear()
    driver.find_element_by_css_selector(".numbers .ic-number").send_keys(quantity)
    driver.find_element_by_css_selector(".numbers .plus-button").click()


if __name__ == "__main__":
    init()
    login()
    buystuff()