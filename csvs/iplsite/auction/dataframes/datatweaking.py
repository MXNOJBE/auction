import pandas as pd

data_2024 ="csvs\\iplsite\\auction\\dataframes\\IPL Teams 2024.csv"

data_2023_dir = "csvs\\iplsite\\auction\\dataframes\\ipl_2023_auction.csv"

data_2023_unsold_dir = 'csvs\\iplsite\\auction\\dataframes\\ipl_2023_unsold.csv'

output_file = 'csvs/iplsite/auction/dataframes/ipl_2023_unsold.csv'
sold_output_file = 'csvs/iplsite/auction/dataframes/ipl_2023_sold.csv'



data_2023  = pd.read_csv(data_2023_dir)

# Filter unsold players (where '2023 Squad' is empty or NaN)
unsoldPlayers2024 = data_2023[data_2023['2023 Squad'].isna() | (data_2023['2023 Squad'] == '')]

# Save unsold players to a CSV file
unsoldPlayers2024.to_csv(output_file, index=False)

# Filter sold players by excluding unsold players
soldPlayers2023 = data_2023[~data_2023['Player Name'].isin(unsoldPlayers2024['Player Name'])]

# Save sold players to a CSV file
soldPlayers2023.to_csv(sold_output_file, index=False)


'''def readData(file):
    df = pd.read_csv(file)
    print(df.columns)

readData(data_2023)
readData(data_2024)'''
