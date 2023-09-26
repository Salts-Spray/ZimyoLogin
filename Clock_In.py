from Login import *

log()

# Path ()
BChkIn = (By.XPATH, "/html/body/div/div/div/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/button/span[1]/h6")

# Clock in
wait.until(EC.presence_of_element_located(BCheck))
wait.until(EC.element_to_be_clickable(BChkIn)).click()

# Browser Sleep
time.sleep(10)

# Close Window
driver.quit()
