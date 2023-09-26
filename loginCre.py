from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Webdriver-manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Redirect to URL
driver.get("https://www.zimyo.work/")

# Variables
logintxt = "9975871746"
passtxt = "#Del120@#908;)"

# Login with Credentials
driver.find_element("xpath","/html/body/div/main/div/div[2]/div/div[2]/form/div/div[1]/div/input").send_keys(logintxt)
time.sleep(2)
driver.find_element("xpath","/html/body/div/main/div/div[2]/div/div[2]/form/div/div[2]/div/input").send_keys(passtxt)
time.sleep(2)
driver.find_element("xpath","/html/body/div/main/div/div[2]/div/div[2]/button[1]/span[1]").click()
time.sleep(10)


# Break Over
# driver.find_element("xpath","/html/body/div/div/div/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[3]/button").click()
# time.sleep(2)
# test
# def login():
#     driver.find_element(By.NAME, 'username').send_keys(logintxt)
#     wait(1)
#     driver.find_element(By.ID, 'password').send_keys('qwerty')
#     wait(1)
#     driver.find_element(By.ID, 'login').click()
#     wait(1)

# Browser Sleep
time.sleep(10)

# Close Window
driver.quit()