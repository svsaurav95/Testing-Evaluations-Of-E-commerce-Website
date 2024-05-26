
#Test for checking that the desired Landing Page is opened for the address 

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
driver.get("https://vercel-commerce.oramasearch.com/")


try:
    WebDriverWait(driver, 10).until(
        EC.title_is("Next.js Commerce")
    )
    # Get page title
    page_title = driver.title
    
    # Verify title
    assert page_title == "Next.js Commerce", f"Expected title to be 'Next.js Commerce' but got '{page_title}'"
    print("Test Passed: Page title is correct.")
except Exception as e:
    print(f"Test Failed: {e}")
finally:
    driver.quit()
