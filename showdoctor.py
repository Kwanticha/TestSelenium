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

icon = driver.find_element(By.ID, 'Home-medical')
icon.click()
time.sleep(4)

link_element = driver.find_element(By.XPATH, "//a[@class='btn btn-success mx-1' and @href='/detaildental/1']")
link_element.click()
time.sleep(3)


Back = driver.find_element(By.ID, "BackshowdepartmentAll")
Back.click()
time.sleep(3)


link_element = driver.find_element(By.XPATH, "//a[@class='btn btn-success mx-1' and @href='/detaildental/2']")
link_element.click()
time.sleep(3)


Back = driver.find_element(By.ID, "BackshowdepartmentAll")
Back.click()
time.sleep(3)


link_element = driver.find_element(By.XPATH, "//a[@class='btn btn-success mx-1' and @href='/detaildental/3']")
link_element.click()
time.sleep(3)


Back = driver.find_element(By.ID, "BackshowdepartmentAll")
Back.click()
time.sleep(3)

link_element = driver.find_element(By.XPATH, "//a[@class='btn btn-success mx-1' and @href='/detaildental/4']")
link_element.click()
time.sleep(3)


Back = driver.find_element(By.ID, "BackshowdepartmentAll")
Back.click()
time.sleep(3)


link_element = driver.find_element(By.XPATH, "//a[@class='btn btn-success mx-1' and @href='/detaildental/6']")
link_element.click()
time.sleep(3)


Back = driver.find_element(By.ID, "BackshowdepartmentAll")
Back.click()
time.sleep(3)


link_element = driver.find_element(By.XPATH, "//a[@class='btn btn-success mx-1' and @href='/detaildental/7']")
link_element.click()
time.sleep(3)


Back = driver.find_element(By.ID, "BackshowdepartmentAll")
Back.click()
time.sleep(3)

link_element = driver.find_element(By.XPATH, "//a[@class='btn btn-success mx-1' and @href='/detaildental/8']")
link_element.click()
time.sleep(3)


Back = driver.find_element(By.ID, "BackshowdepartmentAll")
Back.click()
time.sleep(3)


link_element = driver.find_element(By.XPATH, "//a[@class='btn btn-success mx-1' and @href='/detaildental/23']")
link_element.click()
time.sleep(3)


Back = driver.find_element(By.ID, "BackshowdepartmentAll")
Back.click()
time.sleep(3)


Logo = driver.find_element(By.ID, "HospitalLogo.17")
Logo.click()
time.sleep(2)