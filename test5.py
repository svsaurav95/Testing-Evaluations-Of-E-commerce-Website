
#Test logical functionality of Cart to remove items when Cart is empty 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = "D:/Program Files/chromedriver.exe"

chrome_options = Options()

service = Service(PATH)


driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://shopify.vercel.store/")


try:
    cart_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Open cart']"))
    )
    cart_icon.click()
    empty_cart_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "p.mt-6.text-center.text-2xl.font-bold"))
    )

    # Verify the cart is empty
    assert "Your cart is empty." in empty_cart_message.text, "Cart is not empty!"

    # Check if the remove button is present or clickable
    remove_button_present = False
    try:
        remove_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Reduce item quantity']")
        if remove_button:
            remove_button_present = True
    except:
        remove_button_present = False

    #Check remove button not present 
    assert not remove_button_present, "Remove button should not be present when the cart is empty!"
    

    print("Test Passed: Cannot remove an item when the cart is empty.")
except Exception as e:
    print(f"Test Failed: {e}")
finally:
    driver.quit()
