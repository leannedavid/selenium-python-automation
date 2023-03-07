# Why use wait functions?
# Many websites use asynchronous (like Ajax) techniques to load content, which changes parts of the site without reloading the entire page
# Techinique creates a problem when Selenium tries to located an element that hasn't loaded yet
# Avoid exceptions in scripts
# Wait functions add crucial time intervals in between actions performed.


# Selenium has 2 types of waits: Explicit Wait Functions & Implicit Wait Functions
# Explicit waits, when paired with a condition, will wait until that condition is satisfied before executing
# Implicit waits, will pull DOM for a certain amount of time, until the element becomes available

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://google.com/earth/'
url2 = 'https://twitter.com/'
driver = webdriver.Chrome()
driver.get(url2)

# Create explicit wait; this will thrown an exception after 15 seconds if the condition we make is not satisfied
wait = WebDriverWait(driver, 15)
earthMenuButton = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/a/div/span/span')))
earthMenuButton.click()
time.sleep(5)
driver.quit()