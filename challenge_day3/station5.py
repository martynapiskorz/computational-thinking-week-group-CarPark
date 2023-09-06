import pandas as pd

def solution_station_5(name):
    table_path = "challenge_day3/teamsnames.xlsx"
    df = pd.read_excel(table_path)
    
    try:
        team = df.loc[df['Student firstname'] == name, 'Team'].values[0]
        return team
    except IndexError:
        return "This person is not in the course"
    
    