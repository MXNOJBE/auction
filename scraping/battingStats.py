from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

for year in range(2008, 2025):
    driver.get(f"https://www.iplt20.com/stats/{year}")

    try:
        view_all_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'View All')]"))
        )
        view_all_button.click()
        time.sleep(5)

    except Exception as e:
        print(f"Error clicking 'View All' button for {year}: {e}")
        continue

    try:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        tables = soup.find_all("table")
        dataframes = []
        for table in tables:
            rows = []
            headers = [header.text.strip() for header in table.find_all('th')]

            for row in table.find_all('tr')[1:]:
                cells = [cell.text.strip() for cell in row.find_all('td')]
                if len(cells) == len(headers):
                    rows.append(cells)

            if rows:
                df = pd.DataFrame(rows, columns=headers)
                dataframes.append(df)

        if dataframes:
            final_data = pd.concat(dataframes, ignore_index=True)
            final_data.to_csv(f"ipl_{year}_batting.csv", index=False)
            print(f"Data saved to ipl_{year}_batting.csv")
        else:
            print(f"No tables found on the page for {year}.")

    except Exception as e:
        print(f"Error scraping data for {year}: {e}")
        continue

driver.quit()
