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

driver.get("https://online-web-mauve.vercel.app/")
time.sleep(5)

# เลื่อนหน้าเว็บมายัง Element 'New'
new_element = driver.find_element(By.ID, 'NewsS')
driver.execute_script("arguments[0].scrollIntoView();", new_element)
time.sleep(2)  # รอสักครู่ให้หน้าเว็บเลื่อนมา

link_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID,"Newsdentalservice"))
)

driver.execute_script("arguments[0].click();", link_element)
driver.execute_script("window.scrollBy(0, -1000);")
# รอเว็บไซต์โหลดหน้าใหม่หรือปรับปรุง UI (ปรับเวลาตามความเหมาะสม)
time.sleep(5)

Logo = driver.find_element(By.ID,"HospitalLogo.17")
Logo.click()
time.sleep(5)
# เลื่อนหน้าเว็บมายัง Element 'New'
new_element = driver.find_element(By.ID, 'NewsS')
driver.execute_script("arguments[0].scrollIntoView();", new_element)
time.sleep(2)  # รอสักครู่ให้หน้าเว็บเลื่อนมา

element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID,"Newsfluvaccine"))
)

# หลังจาก Element พร้อมใช้งานแล้วก็คลิก
driver.execute_script("arguments[0].click();", element)
driver.execute_script("window.scrollBy(0, -1000);")
time.sleep(5)

Logo = driver.find_element(By.ID, "HospitalLogo.17")
Logo.click()
time.sleep(5)
new_element = driver.find_element(By.ID, 'NewsS')
driver.execute_script("arguments[0].scrollIntoView();", new_element)
time.sleep(2)  # รอสักครู่ให้หน้าเว็บเลื่อนมา
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID,"NewsModernaBivalent"))
)

# หลังจาก Element พร้อมใช้งานแล้วก็คลิก
driver.execute_script("arguments[0].click();", element)
driver.execute_script("window.scrollBy(0, -1000);")
time.sleep(5)

Logo = driver.find_element(By.ID, "HospitalLogo.17")
Logo.click()
time.sleep(5)

new_element = driver.find_element(By.ID, 'NewsfoodN')
driver.execute_script("arguments[0].scrollIntoView();", new_element)
time.sleep(2)  # รอสักครู่ให้หน้าเว็บเลื่อนมา
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID,"Newsfood"))
)

# หลังจาก Element พร้อมใช้งานแล้วก็คลิก
driver.execute_script("arguments[0].click();", element)
driver.execute_script("window.scrollBy(0, -1000);")
time.sleep(5)

Logo = driver.find_element(By.ID, "HospitalLogo.17")
Logo.click()
time.sleep(2)