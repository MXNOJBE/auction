import re
import pandas as pd

data_2024 ="csvs\\iplsite\\auction\\dataframes\\ipl_2024_soldandunsold.csv"

data_2023_dir = "csvs\\iplsite\\auction\\dataframes\\ipl_2024_soldandunsold.csv"

data_2023_unsold_dir = 'csvs\\iplsite\\auction\\dataframes\\ipl_2023_unsold.csv'

ipl_2024_full_dataset = 'csvs\\iplsite\\auction\\dataframes\\ipl_2024_full.csv'

output_file = 'csvs/iplsite/auction/dataframes/ipl_2024_retention.csv'

#sold_output_file = 'csvs/iplsite/auction/dataframes/ipl_2023_unsold.csv'

# Load Dataset 1 (ipl_2024_full)

'''# Load Dataset 2 (ipl_2024_soldandunsold)
dataset2 = pd.read_csv('csvs\\iplsite\\auction\\dataframes\\ipl_2024_retainedandreleased.csv')

ipl_2024_full = pd.read_csv(ipl_2024_full_dataset)

# Merge Dataset 1 and Dataset 2 on the 'Player' column
merged_dataset = pd.merge(dataset1, dataset2[['Player', 'Status', 'Teams']], on='Player', how='left')'''

#merged_dataset.to_csv('ipl_2024_full_with_status_and_teams.csv', index=False)

dataset1 = pd.read_csv('csvs\\iplsite\\auction\\dataframes\\ipl_2024_retention.csv')
dataset2 = pd.read_csv('csvs\\iplsite\\auction\\dataframes\\ipl_2024_combined_full.csv')  # Dataset with columns Player, Role, Auction Price, Nation, Team

# Define team abbreviation mapping
team_mapping = {
    'Chennai Super Kings': 'CSK',
    'Delhi Capitals': 'DC',
    'Gujarat Titans': 'GT',
    'Kolkata Knight Riders': 'KKR',
    'Lucknow Super Giants': 'LSG',
    'Mumbai Indians': 'MI',
    'Punjab Kings': 'PBKS',
    'Rajasthan Royals': 'RR',
    'Royal Challengers Bangalore': 'RCB',
    'Sunrisers Hyderabad': 'SRH'
}



import pandas as pd

# Load your dataset
dataset1 = pd.read_csv('csvs\\iplsite\\auction\\dataframes\\ipl_2024_full2.csv')

# Apply the mapping and create a new column with the abbreviations
dataset1['Team'] = dataset1['Team'].map(team_mapping).fillna(dataset1['Team'])

# Save the modified DataFrame to a new CSV file
dataset1.to_csv('csvs\\iplsite\\auction\\dataframes\\ipl_2024_full2.csv', index=False)

print("New CSV file created with abbreviated team names.")

'''merged_dataset = pd.merge(dataset1, dataset2[['Player', 'Team']], on='Player', how='left')

# Rename the 'Team' column in the merged dataset to '2024 Squad'
merged_dataset.rename(columns={'Team': '2024 Squad'}, inplace=True)


# Save the modified DataFrame to a new CSV file
dataset1.to_csv('csvs\\iplsite\\auction\\dataframes\\ipl_2024_retention_abbreviated.csv', index=False)


'''

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
