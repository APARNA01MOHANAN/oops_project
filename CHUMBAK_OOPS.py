import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Chumbak:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("http://www.chumbak.com/")

    def login(self):
        self.driver.find_element(By.ID, "user_6_").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.NAME, "customer[email]").send_keys("aparnamohanan@gmail.com")
        self.driver.find_element(By.NAME, "customer[password]").send_keys("aparna_123")
        self.driver.find_element(By.XPATH, "//button[text()='Login']").click()


class Add_to_cart(Chumbak):
    def edit_address(self):
        self.driver.find_element(By.XPATH, "//a[@class='Button Button--primary']").click()
        # after clicking edit address it may go again to the login page so re-run the code
        # it is website issue
        self.driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Add a new address')]").click()
        self.driver.find_element(By.NAME, "address[first_name]").send_keys("Aparna")
        self.driver.find_element(By.NAME, "address[last_name]").send_keys("Mohanan")
        self.driver.find_element(By.NAME, "address[company]").send_keys("APMO")
        self.driver.find_element(By.NAME, "address[phone]").send_keys("9087654395")
        self.driver.find_element(By.NAME, "address[address1]").send_keys("Peruvilai")
        self.driver.find_element(By.NAME, "address[address2]").send_keys("kanyakumari")
        self.driver.find_element(By.NAME, "address[city]").send_keys("Nagercoil")
        select_con = Select(self.driver.find_element(By.CSS_SELECTOR, "select[name='address[country]']"))
        select_con.select_by_visible_text("India")
        self.driver.find_element(By.NAME, "address[zip]").send_keys("629008")
        select_pro = Select(self.driver.find_element(By.CSS_SELECTOR, "select[name='address[province]']"))
        select_pro.select_by_visible_text("Tamil Nadu")
        self.driver.find_element(By.XPATH, "//input[@class='Form__Checkbox']").click()
        self.driver.find_element(By.XPATH,"//button[@class='Form__Submit Button Button--primary Button--full']").click()

    def addproduct(self):

        self.driver.find_element(By.ID, "mm-homepage-search").send_keys("watch")
        time.sleep(6)
        self.driver.find_element(By.XPATH,"//a[contains(normalize-space(),'Mother of Pearl Tropical Beads Watch & Bracelet Set')]").click()
        element = self.driver.find_element(By.CSS_SELECTOR,"button[class='ProductForm__AddToCart Button Button--primary Button--full']")
        self.driver.execute_script("arguments[0].click()", element)
        time.sleep(15)

    def xpath_error(self):
        try:
            self.driver.find_element(By.ID, "uskhgtc_").click()
        except:
            print("You have entered Invalid xpath")


obj = Add_to_cart()

while True:
    print("Enter 1 for login")
    print("Enter 2 to edit address only if you have performed the login function i.e userchoice==1")
    print("Enter 3 to add product ")
    print("Enter 4 to throw error")
    print("Enter 5 to exit")
    userchoice = int(input())
    if userchoice == 1:
        obj.login()
    elif userchoice == 2:
        #while excecuting this line it may go to login page instead of add address it is website error
        #so re-run the code on failure
        obj.edit_address()
    elif userchoice == 3:
        obj.addproduct()
    elif userchoice == 4:
        obj.xpath_error()
    elif userchoice == 5:
        quit()




