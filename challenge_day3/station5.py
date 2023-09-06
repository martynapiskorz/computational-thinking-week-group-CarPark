import pandas as pd

table_path = "challenge_day3/teamsnames.xlsx"

df = pd.read_excel(table_path)

def solution_station_5(name):
    try:
        team = df.loc[df['Student firstname'] == name, 'Team'].values[0]
        return team
    except IndexError:
        return "This person is not in the course"
    
    