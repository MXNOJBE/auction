import re
import pandas as pd

data_2024 ="csvs\\iplsite\\auction\\dataframes\\ipl_2024_soldandunsold.csv"

data_2023_dir = "csvs\\iplsite\\auction\\dataframes\\ipl_2024_soldandunsold.csv"

data_2023_unsold_dir = 'csvs\\iplsite\\auction\\dataframes\\ipl_2023_unsold.csv'

ipl_2024_full_dataset = 'csvs\\iplsite\\auction\\dataframes\\ipl_2024_full.csv'

output_file = 'csvs/iplsite/auction/dataframes/ipl_2024_retained.csv'

#sold_output_file = 'csvs/iplsite/auction/dataframes/ipl_2023_unsold.csv'

# Load Dataset 1 (ipl_2024_full)
dataset1 = pd.read_csv('csvs\\iplsite\\auction\\dataframes\\ipl_2024_rate2.csv')

# Load Dataset 2 (ipl_2024_soldandunsold)
dataset2 = pd.read_csv('csvs\\iplsite\\auction\\dataframes\\ipl_2024_retainedandreleased.csv')

ipl_2024_full = pd.read_csv(ipl_2024_full_dataset)

# Merge Dataset 1 and Dataset 2 on the 'Player' column
merged_dataset = pd.merge(dataset1, dataset2[['Player', 'Status', 'Teams']], on='Player', how='left')

merged_dataset.to_csv('ipl_2024_full_with_status_and_teams.csv', index=False)

'''def clean_price(price):
    return str(price).replace('INR ', '').replace('(R)', '').strip()

# Apply the conversion function
ipl_2024_full['Auction Price (in INR)'] = ipl_2024_full['Auction Price'].apply(clean_price)

# Save to a new CSV file
ipl_2024_full.to_csv(output_file, index=False)

print("Data saved to ipl_2024_full_transformed.csv")'''


'''# Load the data
ipl_2024_full = pd.read_csv('csvs\\iplsite\\auction\\dataframes\\ipl_2024_full.csv')
ipl_2024_soldandunsold = pd.read_csv('csvs\\iplsite\\auction\\dataframes\\ipl_2024_soldandunsold.csv')

# Merge the data on the 'Player' column
combined_data = pd.merge(ipl_2024_full, ipl_2024_soldandunsold, on='Player', how='outer')

# Save the combined data to a new CSV file
combined_data.to_csv(output_file, index=False)

print("Combined CSV file created successfully.")


data_2023  = pd.read_csv(data_2024)
unsoldPlayers2024 = data_2023[data_2023['Status'] != 'UnSold'].to_csv(output_file, index=False)
'''

'''def readData(file):
    df = pd.read_csv(file)
    print(df.columns)

readData(data_2023)
readData(data_2024)'''
