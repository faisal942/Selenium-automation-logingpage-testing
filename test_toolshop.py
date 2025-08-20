import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 



#intialize the varibale with sselected element 
home_url="https://practicesoftwaretesting.com./"
check_button = (By.CLASS_NAME, "icheck")
sigin_btn = (By.CSS_SELECTOR ,"#navbarSupportedContent > ul > li:nth-child(4) > a")


#login page button 
login_Email = (By.ID , "email")
login_Password = (By.ID , "password")
login_btn = (By.CLASS_NAME ,"btnSubmit")
seenpassword = (By.CSS_SELECTOR, "body > app-root > div > app-login > div > div > div > form > div:nth-child(2) > app-password-input > div > div")
card_profuct = (By.CSS_SELECTOR, "body > app-root > div > app-overview > div:nth-child(3) > div.col-md-9 > div.container > a:nth-child(1) > div.card-img-wrapper > img")
login_page= "https://practicesoftwaretesting.com./auth/login" 

# registratiuon section buttons 


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_homepage(driver):
     driver.get(home_url)
    
     assert driver.current_url==(home_url)

  


def test_siginProcess(driver):
     driver.get(home_url)
     time.sleep(3)
     WebDriverWait(driver,10).until(EC.element_to_be_clickable(sigin_btn)).click()
     time.sleep(10)
    #  driver.find_element(By.XPATH,value="/html/body/app-root/app-header/nav/div/div/ul/li[4]/a").click()
    
    

# login the page without registration 
     seembutton =  driver.find_element(*seenpassword)
     driver.find_element(*login_Email).clear()
     driver.find_element(*login_Email).send_keys("faisaliftikhar@gmail.com")
     driver.find_element(*login_Password).send_keys("faisal")
     seembutton =  driver.find_element(*seenpassword)
     seembutton.click()
     time.sleep(10)
     seembutton.click()
     driver.find_element(*login_btn).click()
     driver.find_element(By.XPATH ,'/html/body/app-root/div/app-login/div/div/div/div[3]/p/a[1]').click()
     time.sleep(5)
     

# def test_Home_pageflow_test(driver):
#       driver.get(home_url)
#       WebDriverWait(driver ,5).until(EC.element_to_be_clickable(card_profuct)).click()
#       time.sleep(5)

