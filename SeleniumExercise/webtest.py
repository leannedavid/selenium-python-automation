from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Url to navigate to
url = 'https://google.com/'

# Set up some Chrome options to prevent the test browser from closing after test is done (1 of 2 ways)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Initialize the webdriver for Chrome with the options above
driver = webdriver.Chrome(options=chrome_options)

# Opens a Chrome browser to the url
driver.get(url)

# Different ways to search for the text field
# search = driver.find_element(By.CLASS_NAME, 'gLFyf')
# search = driver.find_element(By.NAME, 'q')
# search = driver.find_element (By.ID, '') # input class doesn't have an id
search = driver.find_element(By.XPATH, '../div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

# Clears the input field of text, if any
search.clear()

# Types our text into the text field
search.send_keys('Selenium exercises')

# Finds the search button to press, same different ways to search for the button
search_button = driver.find_element(By.NAME, 'btnK')

# Presses Enter on the keyboard
search_button.send_keys(Keys.ENTER)

# After a few seconds of the script, it will close and quit the webdriver
driver.quit()