from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Starts the session
driver = webdriver.Chrome()

# Navigates to the url
url = 'https://www.selenium.dev/selenium/web/web-form.html'
driver.get(url)

# Different types of browser information
title = driver.title
current_url = driver.current_url
window_size = driver.current_window_handle
name = driver.name
html = driver.page_source

print('Title: ' + title)
print('Name: ' + name)
print('Current url: ' + current_url)
print('Window size: ' + window_size)
print('Page Source/HTML: ' + html)

driver.quit()