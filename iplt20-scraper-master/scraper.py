from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()  # Replace with your WebDriver path

# Navigate to the IPL T20 website
url = "https://www.iplt20.com/stats/2023"
driver.get(url)

# Wait for the Purple Cap table to load
purple_cap_table = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='cSBListItems bowlers ng-binding ng-scope selected selected1']"))
)

# Click on the Purple Cap tab
purple_cap_tab.click()

# Wait for the table to load
purple_cap_table = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//table[@class='table table-striped']"))
)

# Extract player data
player_data = []
rows = purple_cap_table.find_elements(By.TAG_NAME, "tr")
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    if len(cols) >= 2:
        player_name = cols[0].text
        wickets = cols[1].text
        player_data.append((player_name, wickets))

# Print or store the extracted data
for player in player_data:
    print(player)

# Close the browser
driver.quit()