#if odd then true if even then false

def get_odd(n):
    if n % 2 == 0:
        return "False"
    else:
        return "True"
    
test_number = 7
result = get_odd(test_number)

print(f'{test_number} is {result}')