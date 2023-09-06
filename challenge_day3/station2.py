from datetime import datetime

def solution_station_2(date_in_string):

    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    jap_days = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日', ]

    clean_date = datetime.strptime(date_in_string, '%Y-%m-%d')
    day = clean_date.weekday()

    jap_day = jap_days[day]

    return jap_day

date_in_string = '2023-01-31'
jap_day = solution_station_2(date_in_string)
