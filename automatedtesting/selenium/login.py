# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import time


# Start the browser and login with standard_user
def login(user, password):
    print('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()
    print('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.NAME, 'user-name').send_keys(user)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "login-button").click()
    time.sleep(3)
    title = driver.find_element(By.CLASS_NAME, "title").text
    if title == "Products":
        print("User loggedin successfully...!")
    else:
        print("Error! User login failed...!")
    time.sleep(3)


login('standard_user', 'secret_sauce')
