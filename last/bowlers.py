import pandas as pd

# Load your dataset
data = pd.read_csv('last\deliveries.csv')

# Extract the year from `match_id` if it starts with the year
data['year'] = data['match_id'].astype(str).str[:4].astype(int)

# Filter data to include only relevant columns
bowling_data = data[['year', 'match_id', 'bowler', 'total_runs', 'is_wicket', 'extras_type', 'ball']]

# Remove rows where extras_type is not empty (like legbyes), which means they aren't bowled deliveries
bowling_data = bowling_data[bowling_data['extras_type'].isna()]

# Calculate total matches played by each bowler in each year
matches_played = bowling_data.groupby(['year', 'bowler'])['match_id'].nunique().reset_index(name='matches_played')

# Calculate total runs conceded by each bowler in each year
runs_conceded = bowling_data.groupby(['year', 'bowler'])['total_runs'].sum().reset_index(name='runs_conceded')

# Calculate total wickets taken by each bowler in each year
wickets_taken = bowling_data[bowling_data['is_wicket'] == 1].groupby(['year', 'bowler']).size().reset_index(name='wickets_taken')

# Calculate total balls bowled by each bowler in each year
balls_bowled = bowling_data.groupby(['year', 'bowler']).size().reset_index(name='balls_bowled')

# Merge all the calculated metrics into a single DataFrame
bowler_stats = matches_played.merge(runs_conceded, on=['year', 'bowler'])
bowler_stats = bowler_stats.merge(wickets_taken, on=['year', 'bowler'], how='left').fillna(0)
bowler_stats = bowler_stats.merge(balls_bowled, on=['year', 'bowler'])

# Calculate additional statistics
bowler_stats['average'] = bowler_stats.apply(lambda x: x['runs_conceded'] / x['wickets_taken'] if x['wickets_taken'] > 0 else None, axis=1)
bowler_stats['economy'] = bowler_stats['runs_conceded'] / (bowler_stats['balls_bowled'] / 6)
bowler_stats['strike_rate'] = bowler_stats.apply(lambda x: x['balls_bowled'] / x['wickets_taken'] if x['wickets_taken'] > 0 else None, axis=1)

# Save to a new CSV file
bowler_stats.to_csv('last\\bowler_stats_by_year.csv', index=False)

print("Bowler statistics by year saved to 'bowler_stats_by_year.csv'")
