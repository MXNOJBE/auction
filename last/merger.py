import pandas as pd

# Load the datasets
ball_data = pd.read_csv('last\\deliveries.csv')  # Main dataset with ball-by-ball details
match_data = pd.read_csv('last\\matches_2008-2024.csv')
player_info = pd.read_csv('last\\Players.csv')  # Player details (Player_Name, DOB, Batting_Hand, Bowling_Skill, Country)

# Merge datasets on match_id to bring in the season information
# Merge player data with ball data for batter and bowler details
merged_data = ball_data.merge(player_info[['Player_Name', 'Batting_Hand', 'Bowling_Skill', 'Country']], 
                               left_on='batter', right_on='Player_Name', how='left')

# Create a list of all players who are both batters and bowlers (all-rounders)
allrounders = merged_data[merged_data['Batting_Hand'].notna() & merged_data['Bowling_Skill'].notna()]

# Get batters and bowlers data by excluding all-rounders
batters_data = merged_data[~merged_data['batter'].isin(allrounders['batter'])][['batter', 'Batting_Hand', 'Country']].drop_duplicates()
bowlers_data = merged_data[~merged_data['bowler'].isin(allrounders['bowler'])][['bowler', 'Bowling_Skill', 'Country']].drop_duplicates()

# Combine the batter and bowler data into separate DataFrames for wicketkeepers and others
# Filter for wicketkeepers (Players who are neither batters nor bowlers)
wicketkeepers_data = player_info[(player_info['Batting_Hand'].isna() & player_info['Bowling_Skill'].isna())]

# Remove 'all-rounders' from batters and bowlers lists
batters_data = batters_data[~batters_data['batter'].isin(allrounders['batter'])]
bowlers_data = bowlers_data[~bowlers_data['bowler'].isin(allrounders['bowler'])]

# Rename columns for consistency in output
batters_data.rename(columns={'batter': 'Player_Name'}, inplace=True)
bowlers_data.rename(columns={'bowler': 'Player_Name'}, inplace=True)

# Save data to separate CSV files
batters_data.to_csv('batters_data.csv', index=False)
bowlers_data.to_csv('bowlers_data.csv', index=False)
wicketkeepers_data.to_csv('wicketkeepers_data.csv', index=False)

print("Data saved for batters, bowlers, and wicketkeepers.")