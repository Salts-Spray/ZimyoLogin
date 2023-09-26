from Login import *

log()

# Path (xpath)
BChkOut = "/html/body/div/div/div/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[3]/button[1]/span[1]/h6"

# Clock Out
wait.until(EC.presence_of_element_located(BCheck))
wait.until(EC.element_to_be_clickable((By.XPATH, BChkOut))).click()

# Browser Sleep
time.sleep(10)

# Close Window
driver.quit()