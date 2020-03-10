from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(r"C:\Users\mtaah\Downloads\Python\Selenium\chromedriver")#delete and add your personal path to chromedriver 

driver.get('https://app.reef-education.com/#/login')

#driver.set_page_load_timeout("10")
id_box = driver.find_element_by_id('userEmail')

id_box.send_keys("")#put your useremail

pass_box = driver.find_element_by_id("userPassword")

pass_box.send_keys("")#put your user password

login_box = driver.find_element_by_id("sign-in-button")

login_box.click()

time.sleep(1)
chem = WebDriverWait(driver, 3600).until(ec.visibility_of_element_located((By.XPATH,"//*[contains(text(),'Chem 1AA3 - Moran-Mirabal (C01)')]" )));
chem.click()
join = WebDriverWait(driver, 3600).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div[1]/course-screen-join-session/div/div/div/div[2]/button")));
join.click()


for i in range(0, 1000):

    buttonclick = WebDriverWait(driver, 3600).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div/div/div/div[5]/div[2]/button")));
    buttonclick.click()
    time.sleep(30)
    i += 1

driver.quit()
