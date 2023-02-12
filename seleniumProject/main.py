import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://test-ambor-app-742a2.ondigitalocean.app/")
print(driver.title)

# search = driver.find_element_by_name_()

link = driver.find_elements_by_link_text("Kurti")
link.click()



driver.find_element(By.ID, "").send_keys(password)
sleep(2)

# driver.quit()


# driver.close()