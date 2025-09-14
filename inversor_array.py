a = [1, 2, 3]
b = [3, 2, 1]

def my_solution(a,b):
    for index, i in enumerate(a):
        s = a[index]
        a[index]=b[index]
        b[index]=s 

    print(a)
    print(b)

def another_solution(a,b):
    temp = a
    a = b
    b = temp

    print(a)
    print(b)

