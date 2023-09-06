#if divisable by 3 then true, the rest is false

def solution_station_3(n):
    if n == 0:
        print ("True")
    if n%3 == 0:
        print('True')
    else:
        print('False')
    
    
solution_station_3(6)