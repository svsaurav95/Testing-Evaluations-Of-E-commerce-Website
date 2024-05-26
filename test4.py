
#Test to check if clicking on product leads to correct page with the product info

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
    
    shirt_anchor = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/product/acme-geometric-circles-t-shirt']"))
    )
    shirt_anchor.click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "meta[property='og:title'][content='Acme Circles T-Shirt | Acme Store']"))
    )
    print("The anchor tag leads to the correct landing page.")
    
    # Assertion to validate the test case
    meta_title = driver.find_element(By.CSS_SELECTOR, "meta[property='og:title'][content='Acme Circles T-Shirt | Acme Store']")
    assert meta_title is not None, "Landing page title does not match!"
    print("Test Passed: The landing page title is correct.")
except Exception as e:
    print(f"Test Failed: {e}")
finally:
    driver.quit()
