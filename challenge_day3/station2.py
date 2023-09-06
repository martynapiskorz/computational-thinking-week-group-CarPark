from datetime import datetime

def get_day(date_in_string):
    clean_date = datetime.strptime(date_in_string, '%Y-%m-%d')
    day = clean_date.weekday()
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    return days[day]

date_in_string = '2023-01-01'
english_day = get_day(date_in_string)

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
chinese_days = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日', ]

for i in range(len(days)):
        day1 = days[i]
        day2 = chinese_days[i]
        print(f"{day1}: {day2}")