# Imports
import os
from selenium import webdriver

# Globals
chromedriver_path = os.getcwd() + "/.selenium/drivers/chromedriver"

# Logic
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get('https://home.softtek.com')

username = driver.find_element_by_name("loginfmt")
username.clear()
username.send_keys("germann.gonzalez@softtek.com")

driver.find_element_by_id("idSIButton9").click()