def solution_station_7(expression):
    variables = {'a': 3, 'b' : -1, 'c' : 4, 'd' : 7, 'e' : 0.5}
   
    for var, val in variables.items():
        expression = expression.replace(var, str(val))

    return print(eval(expression))


    