from idlelib import browser

import selenium
selenium.webdriver.support.ui.Select
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path='C:\Program Files (x86)\geckodriver.exe')


driver.get('https://test-ambor-app-742a2.ondigitalocean.app/product/Nirupoma---Salwar-Kamiz/details/?spm=328')
select=browser.find_element(by=By.XPATH, value="//option[normalize-space()='Green']")
select.send_keys("Green")

res = driver.find_element(By.XPATH, "(//button[normalize-space()='Add to Cart'])[1]")
res.click()
