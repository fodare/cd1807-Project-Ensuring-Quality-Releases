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
    print('Browser started successfully. Navigating to the demo page to login.\n')
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.NAME, 'user-name').send_keys(user)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "login-button").click()
    time.sleep(3)
    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"
    if title == "Products":
        print("User loggedin successfully...!\n")
    else:
        print("Error! User login failed...!\n")
    time.sleep(3)


def add_and_remove_cartItems(user, password):
    """Adds and removes cart items."""
    print("Starting cart item test....!")
    options = ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()
    print('Browser started successfully. Navigating to product catalog...!\n')
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.NAME, 'user-name').send_keys(user)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "login-button").click()
    title = driver.find_element(By.CLASS_NAME, "title").text
    if title == "Products":
        print("Successfully navigated to the products page!\n")
    else:
        print("Error!. Can not load product catlog!\n")
    driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.NAME, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(
        By.NAME, "add-to-cart-sauce-labs-fleece-jacket").click()
    driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(
        By.NAME, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
    print("Added all products to cart.\n")

    cart_item_count = driver.find_element(
        By.CLASS_NAME, "shopping_cart_badge").text
    assert int(cart_item_count) == 6
    if int(cart_item_count) == 6:
        print(f"Cart item count: {cart_item_count}")
    else:
        print("Error! Cart item count is not equal to 6!\n")

    print("Removing cart items .....!\n")
    driver.find_element(By.NAME, "remove-sauce-labs-backpack").click()
    driver.find_element(By.NAME, "remove-sauce-labs-bike-light").click()
    driver.find_element(By.NAME, "remove-sauce-labs-bolt-t-shirt").click()
    driver.find_element(
        By.NAME, "remove-sauce-labs-fleece-jacket").click()
    driver.find_element(By.NAME, "remove-sauce-labs-onesie").click()
    driver.find_element(
        By.NAME, "remove-test.allthethings()-t-shirt-(red)").click()
    if driver.find_element(By.CLASS_NAME, "shopping_cart_link"):
        print(f"Successfully removed cart items!")
    else:
        ("Error! Cart item not empty!.")
    time.sleep(2)


login('standard_user', 'secret_sauce')
add_and_remove_cartItems('standard_user', "secret_sauce")
