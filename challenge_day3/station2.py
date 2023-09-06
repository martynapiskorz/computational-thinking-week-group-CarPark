from datetime import datetime

def get_day(date_in_string):
    clean_date = datetime.strptime(date_in_string, '%Y-%m-%d')
    day = clean_date.weekday()
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    return days[day]

date_in_string = 2023-01-01
english_day = get_day(date_in_string)

print(english_day)