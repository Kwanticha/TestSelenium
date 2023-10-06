from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import unittest

class ManageSymptomTest(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome WebDriver
        s = Service('D:\webdriver\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)

    def tearDown(self):
        # Close the browser
        self.driver.quit()

    def test_ManageSymptom_in_Q_Online(self):
        # Open the web application
        self.driver.get("https://online-web-mauve.vercel.app/")
        # คลิกปุ่ม "เข้าสู่ระบบ"
        open_modal_button = self.driver.find_element(By.ID, "loginNavbar")
        open_modal_button.click()
     
        # ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
        id_input = self.driver.find_element(By.ID, "LoginID_Card")
        password_input = self.driver.find_element(By.ID, "LoginPassword")

        # กรอกข้อมูลใน input field
        id_input.send_keys("1789789548789")
        password_input.send_keys("123456")

        # Wait for the search results to load
        time.sleep(5)

        # คลิกปุ่ม "เข้าสู่ระบบ"
        login_button = self.driver.find_element(By.ID, "Login")
        login_button.click()

        time.sleep(4)

        icon = self.driver.find_element(By.ID, 'Home-Queue')
        icon.click()
        time.sleep(5)
        button = self.driver.find_element(By.ID, 'EditQueue')
        button.click()
        time.sleep(5)

        input_element = self.driver.find_element(By.ID, "Editsymptom")
        input_element.clear()
        input_element.send_keys('แก้มบวม ปวดฟันมาก ๆ เจ็บปาก')
        time.sleep(5)

        # คลิกปุ่ม
        button_element = self.driver.find_element(By.ID, "QSubmit")

        # คลิกปุ่ม
        button_element.click()
        time.sleep(2)

    def test_search_in_google2(self):

        self.driver.get("https://online-web-mauve.vercel.app/")

        open_modal_button = self.driver.find_element(By.ID, "loginNavbar")
        open_modal_button.click()

        id_input = self.driver.find_element(By.ID, "LoginID_Card")
        password_input = self.driver.find_element(By.ID, "LoginPassword")

        # กรอกข้อมูลใน input field
        id_input.send_keys("1789789548789")
        password_input.send_keys("123456")

        # Wait for the search results to load
        time.sleep(5)

        # คลิกปุ่ม "เข้าสู่ระบบ"
        login_button = self.driver.find_element(By.ID, "Login")
        login_button.click()

        time.sleep(4)

        icon = self.driver.find_element(By.ID, 'Home-Queue')
        icon.click()
        time.sleep(5)
        button = self.driver.find_element(By.ID, 'EditQueue')
        button.click()
        time.sleep(5)

        input_element = self.driver.find_element(By.ID, "Editsymptom")
        input_element.send_keys(Keys.BACK_SPACE * len(input_element.get_attribute("value")))
        time.sleep(5)

        # ค้นหาอิลิเมนต์ button โดยใช้ attribute type="submit"
        button_element = self.driver.find_element(By.ID, "QSubmit")

        # คลิกปุ่ม
        button_element.click()
        time.sleep(6)

if __name__ == "__main__":
    unittest.main()
