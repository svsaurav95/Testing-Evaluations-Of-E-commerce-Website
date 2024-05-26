
#Test for implementing a seach bar analysis by searcing an element and verifying results

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
    
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='search']"))
    )

    # Enter the search element 
    search_term = "jacket"
    search_input.send_keys(search_term)

    # Submit
    search_input.submit()
    

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.grid"))
    )
    
    print(f"Search for '{search_term}' works and results are displayed.")
    
    # Assertion to validate the test case
    results = driver.find_elements(By.CSS_SELECTOR, "div.grid div")
    assert len(results) > 0, "No search results found!"
    print(f"Test Passed: Search results for '{search_term}' are displayed correctly.")
except Exception as e:
    print(f"Test Failed: {e}")
finally:
    
    driver.quit()
