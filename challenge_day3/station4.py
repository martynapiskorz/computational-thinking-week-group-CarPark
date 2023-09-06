def solution_station_4(n):
    if n % 2 == 0:
        return "False"
    else:
        return "True"
    
test_number = 7
result = solution_station_4(test_number)

print(f'{test_number} is {result}')