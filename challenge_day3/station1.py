def solution_station_1(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x+y
    return x
