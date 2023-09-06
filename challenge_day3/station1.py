def solution_station_1(n):
    n=int(n)
    l = [0, 1]
    i = 2
    while i <= n:
        l.append(l[-1] + l[-2])
        i += 1
    return l[-1]

