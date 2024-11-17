import pandas as pd

# Sample data (replace with actual data)
data = pd.read_csv("last\\combined_player_stats.csv")


# Define the column names based on your format
columns = [
    "Player_Name_batting", "matches_played_batting", "runs_scored", "balls_faced", "strike_rate_batting", "average", 
    "Player_Name_batting", "Batting_Hand", "Country_batting", "bowler", "matches_played_bowling", "runs_conceded", 
    "overs_bowled", "wickets_taken", "economy_rate", "strike_rate_bowling", "Player_Name_bowling", "Bowling_Skill", 
    "Country_bowling"
]

# Create a DataFrame
df = pd.DataFrame(data, columns=columns)

# Fix duplicate column names by renaming them distinctly
df.columns = [
    "Player_Name_batting", "matches_played_batting", "runs_scored", "balls_faced", "strike_rate_batting", "average", 
    "Player_Name_batting_2", "Batting_Hand", "Country_batting", "bowler", "matches_played_bowling", "runs_conceded", 
    "overs_bowled", "wickets_taken", "economy_rate", "strike_rate_bowling", "Player_Name_bowling", "Bowling_Skill", 
    "Country_bowling"
]

# Separate batting and bowling data
batting_columns = ['Player_Name_batting', 'matches_played_batting', 'runs_scored', 'balls_faced', 'strike_rate_batting', 'average', 'Batting_Hand', 'Country_batting']
bowling_columns = ['bowler', 'matches_played_bowling', 'runs_conceded', 'overs_bowled', 'wickets_taken', 'economy_rate', 'strike_rate_bowling', 'Player_Name_bowling', 'Bowling_Skill', 'Country_bowling']

# Create separate DataFrames for batters and bowlers
batters_df = df[batting_columns].rename(columns={"Player_Name_batting": "Player_Name", "Country_batting": "Country"})
bowlers_df = df[bowling_columns].rename(columns={"Player_Name_bowling": "Player_Name", "Country_bowling": "Country"})

# Fill in "NA" for missing values in bowler or batter sections
batters_df['matches_played_batting'].fillna("NA", inplace=True)
bowlers_df['matches_played_bowling'].fillna("NA", inplace=True)

# Create sets of player names from batters and bowlers
batters_set = set(batters_df['Player_Name'])
bowlers_set = set(bowlers_df['Player_Name'])

# Identify all-rounders (players appearing in both batting and bowling)
allrounders_set = batters_set.intersection(bowlers_set)

# Create DataFrames for all-rounders, batters, and bowlers
allrounders_df = df[df['Player_Name_batting_2'].isin(allrounders_set)].copy()
batters_only_df = df[~df['Player_Name_batting_2'].isin(allrounders_set)].copy()
bowlers_only_df = df[~df['Player_Name_bowling'].isin(allrounders_set)].copy()

# Remove "NA" rows in player names
allrounders_df = allrounders_df.dropna(subset=["Player_Name_batting_2"])
batters_only_df = batters_only_df.dropna(subset=["Player_Name_batting"])
bowlers_only_df = bowlers_only_df.dropna(subset=["Player_Name_bowling"])

# Save DataFrames to CSVs
allrounders_df.to_csv('allrounders.csv', index=False)
batters_only_df.to_csv('batters.csv', index=False)
bowlers_only_df.to_csv('bowlers.csv', index=False)

print("CSV files have been created: 'allrounders.csv', 'batters.csv', 'bowlers.csv'.")