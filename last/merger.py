import pandas as pd

# Load the datasets
ball_data = pd.read_csv('last\\deliveries.csv')  # Main dataset with ball-by-ball details
match_data = pd.read_csv('last\\matches_2008-2024.csv')
player_info = pd.read_csv('last\\Players.csv')  # Player details (Player_Name, DOB, Batting_Hand, Bowling_Skill, Country)

# Merge datasets on match_id to bring in the season information
merged_data = ball_data.merge(match_data[['id', 'season']], left_on='match_id', right_on='id', how='left')

# Merge the player data to get designation and country information
merged_data = merged_data.merge(player_info[['Player_Name', 'Batting_Hand', 'Bowling_Skill', 'Country']], 
                                 left_on='batter', right_on='Player_Name', how='left')

# Ensure the 'is_wicket' column exists and replace NaN with 0 for non-wicket balls
merged_data['is_wicket'] = merged_data['is_wicket'].fillna(0).astype(int)

# Batting Stats Calculation (For each batter)
batting_stats = merged_data.groupby('batter').apply(lambda x: pd.Series({
    'matches_played': x['match_id'].nunique(),
    'runs_scored': x['batsman_runs'].sum(),
    'balls_faced': len(x),
    'strike_rate': (x['batsman_runs'].sum() / len(x)) * 100 if len(x) > 0 else "NA",
    'average': x['batsman_runs'].sum() / len(x) if len(x) > 0 else "NA"
})).reset_index()

# Bowling Stats Calculation (For each bowler)
bowling_stats = merged_data.groupby('bowler').apply(lambda x: pd.Series({
    'matches_played': x['match_id'].nunique(),
    'runs_conceded': x['total_runs'].sum(),
    'overs_bowled': len(x) / 6,  # Since each ball is recorded, dividing by 6 gives overs
    'wickets_taken': x['is_wicket'].sum(),
    'economy_rate': (x['total_runs'].sum() / (len(x) / 6)) if len(x) > 0 else "NA",  # Runs per over
    'strike_rate': (len(x) / x['is_wicket'].sum()) if x['is_wicket'].sum() > 0 else "NA"  # Balls per wicket
})).reset_index()

# Merge batting stats with player roles and country
batting_stats = batting_stats.merge(player_info[['Player_Name', 'Batting_Hand', 'Country']], 
                                    left_on='batter', right_on='Player_Name', how='left')

# Merge bowling stats with player roles and country
bowling_stats = bowling_stats.merge(player_info[['Player_Name', 'Bowling_Skill', 'Country']], 
                                     left_on='bowler', right_on='Player_Name', how='left')

# Replace NaN values with 'NA' for missing stats
batting_stats.fillna('NA', inplace=True)
bowling_stats.fillna('NA', inplace=True)

# Combine batting and bowling stats into one final DataFrame
final_data = pd.merge(batting_stats, bowling_stats, how='outer', left_on='batter', right_on='bowler', 
                       suffixes=('_batting', '_bowling'))

# Save combined data to a CSV file
final_data.to_csv('combined_player_stats.csv', index=False)

print("Combined player stats saved to 'combined_player_stats.csv'")
