import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestChumbak:
    @pytest.fixture
    def driver(self, request):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(30)
        request.addfinalizer(driver.quit)
        driver.get("http://www.chumbak.com/")
        return driver
    def test_login(self, driver):
        driver.find_element(By.ID, "user_6_").click()
        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.NAME, "customer[email]").send_keys("aparnamohanan@gmail.com")
        driver.find_element(By.NAME, "customer[password]").send_keys("aparna_123")
        driver.find_element(By.XPATH, "//button[text()='Login']").click()
        expected_header = 'Primary Address'
        element = driver.find_element(By.XPATH, "//h2[normalize-space()='Primary address']")
        assert expected_header in element.text

    @pytest.mark.skip(reason="Still to Enhance")
    def test_addproduct(self,driver):
        driver.find_element(By.ID, "mm-homepage-search").send_keys("watch")
        time.sleep(6)
        driver.find_element(By.XPATH,"//a[contains(normalize-space(),'Mother of Pearl Tropical Beads Watch & Bracelet Set')]").click()
        element = driver.find_element(By.CSS_SELECTOR,"button[class='ProductForm__AddToCart Button Button--primary Button--full']")
        driver.execute_script("arguments[0].click()", element)
        time.sleep(15)

