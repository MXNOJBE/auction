from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Configure Selenium WebDriver
driver = webdriver.Chrome()

# Navigate to the initial page
driver.get("https://datawrapper.dwcdn.net/qtbMh/9/")
time.sleep(3)  # Wait for the page to load

all_data = []

try:
    page_number = 1  # Start with the first page
    while True:
        print(f"Scraping page {page_number}...")

        # Extract table data from the current page
        try:
            table = driver.find_element(By.TAG_NAME, "table")
            rows = table.find_elements(By.TAG_NAME, "tr")
            page_data = [
                [cell.text for cell in row.find_elements(By.TAG_NAME, "td")]
                for row in rows
            ]

            # Add only non-empty rows
            page_data = [row for row in page_data if row]
            all_data.extend(page_data)
        except NoSuchElementException:
            print("Table not found on this page.")
            break

        # Wait and look for the "Next" button using dynamic XPath
        try:
            # Use different XPath based on the page number
            if page_number == 1:
                next_button_xpath = "//*[@id='chart']/div/div/div[1]/div[2]/button"  # For page 1
            else:
                next_button_xpath = "/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button[2]"  # For subsequent pages

            # Wait until the "Next" button is clickable with the appropriate XPath
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, next_button_xpath))
            )
            
            # Check if "Next" button is still there, and break if not
            if next_button.is_enabled():
                next_button.click()
                time.sleep(3)  # Adjust the sleep time based on the site's responsiveness
                page_number += 1
            else:
                print("No more pages to navigate.")
                break
        except NoSuchElementException:
            print("No more pages to navigate.")
            break
        except Exception as e:
            print(f"Error during page navigation: {e}")
            break

finally:
    driver.quit()

# Determine the number of columns dynamically
if all_data:
    num_columns = max(len(row) for row in all_data)
    columns = [f"Column{i+1}" for i in range(num_columns)]  # Generate placeholder column names

    # Convert to DataFrame
    df = pd.DataFrame(all_data, columns=columns)

    # Save to a CSV file
    df.to_csv("ipl_auction_data.csv", index=False)
    print("Data saved to ipl_auction_data.csv")
else:
    print("No data was extracted.")
