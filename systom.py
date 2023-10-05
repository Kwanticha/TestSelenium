from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select


# ระบุพาธของ ChromeDriver 
chrome_driver_path = "D:\webdriver/chromedriver.exe"

# เริ่มต้น WebDriver
driver = webdriver.Chrome()
# ขยายหน้าต่างเบราว์เซอร์ให้เต็มหน้าจอ
driver.maximize_window()

# เปิดเว็บไซต์ของคุณ
driver.get("https://online-web-mauve.vercel.app/")
# คลิกปุ่ม "เข้าสู่ระบบ"
open_modal_button = driver.find_element(By.ID, "loginNavbar")
open_modal_button.click()

# ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
id_input = driver.find_element(By.ID,"LoginID_Card")
password_input = driver.find_element(By.ID, "LoginPassword")

# กรอกข้อมูลใน input field
id_input.send_keys("1789789548789")
password_input.send_keys("123456")

time.sleep(2)

# คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
login_button = driver.find_element(By.ID, "Login")
login_button.click()

# รอสักครู่เพื่อให้หน้าเว็บโหลดและดำเนินการต่อ
time.sleep(4) 

icon = driver.find_element(By.ID, 'Home-Queue')
icon.click()
time.sleep(5)




button = driver.find_element(By.ID, 'EditQueue')
button.click()
time.sleep(5)

input_element = driver.find_element(By.ID, "Editsymptom")
input_element.clear()
input_element.send_keys('แก้มบวม ปวดฟัน ')
time.sleep(5)


# ค้นหาอิลิเมนต์ button โดยใช้ attribute type="submit"
button_element = driver.find_element(By.ID, "QSubmit")

# คลิกปุ่ม
button_element.click()
time.sleep(6)

