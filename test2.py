
#Test to check the Price sorting Filter and see if values are in correct order from low to high price ranges
# or if a valid price is not available show error 

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
driver.get("https://vercel-commerce.oramasearch.com/search/shirts?sort=price-asc")

try:
    
    price_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "p.flex-none.rounded-full.bg-blue-600.p-2.text-white"))
    )
    # if less than 2 prices, cannot compare 
    if len(price_elements) < 2:
        print("Pricing error: Not enough price elements found.")
    else:
        #Conv price elements to float
        price_1 = price_elements[0].text.strip("$")
        price_2 = price_elements[1].text.strip("$")
        
        try:
            price_1_value = float(price_1)
            price_2_value = float(price_2)
            
            # Compare the prices
            if price_1_value < price_2_value:
                print("Price filtering is correct.")
            else:
                print("Incorrect price filtering.")
        except ValueError:
            print("Pricing error: Unable to determine the price values.")
except Exception as e:
    print(f"Test Failed: {e}")
finally:
    # Close the WebDriver
    driver.quit()
