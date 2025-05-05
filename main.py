import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(2)

# Go to webpage
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(3)

# Type username student into Username field
username_locator = driver.find_element(By.ID, "username")
username_locator.send_keys("student")

# Type password Password123 into Password field
password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
username_locator.send_keys("Password123")

# Push Submit button
button_locator = driver.find_element(By.XPATH, "//button[@id='submit']")
button_locator.click()
time.sleep(3)

# Verify new page URL contains practicetestautomation.com/logged-in-successfully/
actual_url = driver.current_url
assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
congratulation_locator = driver.find_element(By.TAG_NAME, "h1")
text = congratulation_locator.text
assert text == "Logged In Successfully"

# Verify button Log out is displayed on the new page
logout_locator = driver.find_element(By.LINK_TEXT, "Log out")
assert logout_locator.is_displayed()


