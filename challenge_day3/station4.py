def solution_station_4(n):
    if n == 1:
        return False
    elif n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False
