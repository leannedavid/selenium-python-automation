# webdriver is a browser that selenium usess to interact with the web
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# OPTIONAL: to supressed the log messages from the console
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
# to supress the error messages/logs
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options) # Can exclude options entirely
driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

# XPath is element specific and allows Selenium to find the HTML item
# Right-click on the message field in the browser > Inspect > Right-click on the highlighted HTML code > Copy > Copy XPath
messageField = driver.find_element(By.XPATH, '//*[@id="user-message"]')

# send_keys sends our message to the input field above
messageField.send_keys('Hello, World!')

# Finds the Submit button
showMessageButton = driver.find_element(By.XPATH, '//*[@id="get-input"]/button')

# Clicks the submit button
showMessageButton.click()

# Leaves the browser open for 5 secs the user to see what is happening before the browser automatically closes
time.sleep(5)

###################

a_field = driver.find_element(By.XPATH, '//*[@id="sum1"]')
a_field.send_keys('5')

b_field = driver.find_element(By.XPATH, '//*[@id="sum2"]')
b_field.send_keys('10')

getTotalButton = driver.find_element(By.XPATH, '//*[@id="gettotal"]/button')
getTotalButton.click()
time.sleep(5)

driver.quit()