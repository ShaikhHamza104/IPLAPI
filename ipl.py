import pandas as pd
import numpy as np

matches = pd.read_csv('dataset/matches_cleaned.csv')

def get_valid_teams():
    """Retrieves unique team names from both 'team1' and 'team2' columns."""
    team_names = set(matches['team1']).union(set(matches['team2']))
    return sorted(team_names)

def all_teams():
    """Retrieves all unique team names from the dataset."""
    return {'teams': get_valid_teams()}

def teamVteamAPI(team1, team2):
    """Analyzes matches between two teams."""
    valid_teams = get_valid_teams()
    
    if team1 not in valid_teams or team2 not in valid_teams:
        return {'error': 'Invalid team names. Please enter valid team names.'}

    teamvteam = matches[(matches['team1'] == team1) & (matches['team2'] == team2) |
                        (matches['team1'] == team2) & (matches['team2'] == team1)]

    total_matches = len(teamvteam)

    # Handle KeyError if a team has never won
    win1 = teamvteam['winner'].value_counts().get(team1, 0)
    win2 = teamvteam['winner'].value_counts().get(team2, 0)
    draw = total_matches - (win1 + win2)

    return {
        'total_matches': str(total_matches),
        'team1_wins': str(win1),
        'team2_wins': str(win2),
        'draws': str(draw)
    }
