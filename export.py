from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()

driver.get("https://www.twitch.tv/robosteph/manager")

print(driver.title)

# inputElement = driver.find_element_by_name("q")

# inputElement.send_keys("cat")

# inputElement.submit()

# try:
# 	WebDriverWait(driver, 10).until(expected_conditions.title_contains("cat"))

# 	print(driver.title)

# finally:
# 	driver.quit()



####NOTES
#Look into using Get Video API to get video info for posting