import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class DemoFindElementsID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        url = "https://test-ambor-app-742a2.ondigitalocean.app/login"
        driver.get(url)
        # driver.exit()
        # driver.find_elements(By.CSS_SELECTOR, "#phone_number").send_keys("01521503628")
        driver.find_element(By.XPATH, "//input[@id='phone_number']").send_keys("2322")

        time.sleep(4)

findbyid = DemoFindElementsID()
findbyid.locate_by_id_demo()



