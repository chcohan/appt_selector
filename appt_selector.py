from selenium import webdriver
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


def walmart(username,password):

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



if __name__ == "__main__":
    
    USER = os.environ['walgreens_username']
    PASS = os.environ['walgreens_password']
    walgreens(USER, PASS)
    walmart(USER,PASS)