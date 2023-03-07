from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()
driver.maximize_window() # maximizes the window
driver.get('http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

source = driver.find_element(By.XPATH, '//*[@id="box3"]')
destination = driver.find_element(By.XPATH, '//*[@id="box103"]')

# Action Chains extends Selenium by allowing the web driver to perform more complex tasks like drag n' drop
# When methods are called for actions on the actions chains object, the actions are stored in a queue

actions = ActionChains(driver)

# To execute actions on the actions object, we use perform which fires the events in the order they were queued.
actions.drag_and_drop(source, destination).perform()
time.sleep(5)

driver.quit()