import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select




def login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get("http://www.chumbak.com/")
    driver.find_element(By.ID, "user_6_").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element(By.NAME, "customer[email]").send_keys("aparnamohanan@gmail.com")
    driver.find_element(By.NAME, "customer[password]").send_keys("aparna_123")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    return("success")


