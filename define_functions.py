value1 = float(input("Digite o primeiro número: "))
value2 = float(input("Digite o segundo número: "))
value3 = float(input("Digite o terceiro número: "))

def least_diference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a-b)
    diff2 = abs(a-c)
    diff3 = abs(c-b)
    return min(diff1, diff2, diff3)



print(least_diference(value1, value2, value3))




