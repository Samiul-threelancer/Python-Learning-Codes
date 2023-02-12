from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://test-ambor-app-742a2.ondigitalocean.app/kurti/Anjona---Kurti/details/?spm=383')


res = driver.find_element(By.CSS_SELECTOR, ".btn.cart_add")
res.click()

dropDownBox = driver.find_element(by = By.TAG_NAME, value="option")
dropDownBox[0].click()

cartAdd = driver.find_element(By.CSS_SELECTOR, ".btn.cart_add")
cartAdd.click()







time.sleep(1)

driver.close()