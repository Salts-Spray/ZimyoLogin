from Login import *

log()

# Path (xpath)
BResume = "//*[@id='root']/div/div/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[3]/button"

# Resume
wait.until(EC.presence_of_element_located(BCheck))
wait.until(EC.element_to_be_clickable((By.XPATH, BResume))).click()

# Browser Sleep
time.sleep(10)

# Close Window
driver.quit()