from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)



driver.get("https://www.messenger.com/")
time.sleep(5)
email=driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div[1]/div/div[2]/div/div[7]/div[1]/div/div[2]/div[1]/div/form/div/input[6]")
email.send_keys("gikan59083@epeva.com")
time.sleep(5)
pwd=driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div[1]/div/div[2]/div/div[7]/div[1]/div/div[2]/div[1]/div/form/div/input[7]")
pwd.send_keys("949802")
time.sleep(5)
ent=driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div[1]/div/div[2]/div/div[7]/div[1]/div/div[2]/div[1]/div/form/div/div[1]/button")
ent.send_keys(Keys.RETURN)
