from Login import *

log()

# Path (xpath)
BBrk = "/html/body/div/div/div/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[3]/button[2]/span[1]/h6"

# Break
wait.until(EC.presence_of_element_located(BCheck))
wait.until(EC.element_to_be_clickable((By.XPATH, BBrk))).click()

# Browser Sleep
time.sleep(5)

# Close Window
driver.quit()
