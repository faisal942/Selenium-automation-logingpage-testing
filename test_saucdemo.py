import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Login_URL = "https://www.saucedemo.com/v1/"
Home_url = "https://www.saucedemo.com/v1/inventory.html"
USERNAME = (By.ID, "user-name")
PASSWORD = (By.ID, "password")
LOGIN_BTN = (By.ID, "login-button")
INVENTORY_CONTAINER = (By.CLASS_NAME, "inventory_list")
HamBurger = (By.CLASS_NAME, "bm-burger-button")
About_page = (By.ID,"about_sidebar_link")
add_product = (By.NAME ,"ADD TO CART")

@pytest.fixture
def driver():
    # Make sure chromedriver is in your PATH, or provide the path to ChromeDriver here.
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def check_box(driver):
    driver.get(Home_url)
 #   WebDriverWait(driver, 5).until(EC.visibility_of_element_located(USERNAME))
    assert driver.current_url == Login_URL

     
def test_login_flow(driver):
    # 1) Open home page and assert URL
    driver.get(Login_URL)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(USERNAME))
    assert driver.current_url == Login_URL

    # 2) Enter credentials and submit
    driver.find_element(*USERNAME).clear()
    driver.find_element(*USERNAME).send_keys("standard_user")   # known saucedemo test user
    driver.find_element(*PASSWORD).clear()
    driver.find_element(*PASSWORD).send_keys("secret_sauce")
    driver.find_element(By.LINK_TEXT,"inventory.html").click()

    # 3) Wait for inventory page to load and verify
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INVENTORY_CONTAINER))
    assert "inventory" in driver.current_url  
    # optional extra check: assert at least one product is visible
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) > 0, "No products found on inventory page; login might have failed."



    WebDriverWait(driver ,5).until(EC.element_to_be_clickable(HamBurger)).click()
    WebDriverWait(driver,5).until(EC.element_to_be_clickable(About_page)).click()
    WebDriverWait(driver ,10 ).until(EC.element_to_be_clickable(add_product)).click()
    

     

def test_Hamburger(driver):
    driver.get(Home_url)
    
    WebDriverWait(driver ,5).until(EC.element_to_be_clickable(HamBurger)).click()
    WebDriverWait(driver,5).until(EC.element_to_be_clickable(About_page)).click()