from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

def walgreens(username,password):

    driver = webdriver.Chrome('C:\\Users\\charl\\Downloads\\chromedriver_win32\\chromedriver.exe')

    # enter vaccination into search bar and click
    driver.get('https://www.walgreens.com/findcare/vaccination/covid-19')
    click_get_started = driver.find_element_by_xpath('//*[@id="userOptionButtons"]/a')
    click_get_started.click()

    # enter username
    username_field = driver.find_element_by_xpath('//*[@id="user_name"]')
    username_field.send_keys(username)

    # enter password
    pass_field = driver.find_element_by_xpath('//*[@id="user_password"]')
    pass_field.send_keys(password)

    # click submit
    click_sign_in = driver.find_element_by_xpath('//*[@id="submit_btn"]')
    click_sign_in.click()

    
    # while True:
    #     pass


def walmart(username,password,zipcode):

    driver = webdriver.Chrome('C:\\Users\\charl\\Downloads\\chromedriver_win32\\chromedriver.exe')
    # enter vaccination into search bar and click
    driver.get('https://www.walmart.com/pharmacy/clinical-services/immunization/scheduled?imzType=covid')

    # enter username
    username_field = driver.find_element_by_xpath('//*[@id="email"]')
    username_field.send_keys(username)

    # enter password
    pass_field = driver.find_element_by_xpath('//*[@id="password"]')
    pass_field.send_keys(password)

    # click submit
    click_sign_in = driver.find_element_by_xpath('//*[@id="sign-in-form"]/button[1]')
    click_sign_in.click()

    # update zipcode
    zipcode_field_xpath = "//*[@id = 'zipcode-form-input']"

    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//*[@id = 'zipcode-form-input']/iframe")))

    zipcode_field = driver.find_element_by_xpath(zipcode_field_xpath)
    zipcode_field.send_keys(zipcode)
        
    while True:
        pass


if __name__ == "__main__":
    
    USER = os.environ['walgreens_username']
    PASS = os.environ['walgreens_password']
    ZIP = os.environ['zipcode']
    #walgreens(USER, PASS)
    walmart(USER,PASS,ZIP)