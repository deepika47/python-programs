def multiple(a, b):
    a = range(b, (a * b)+1, b)
    print(*a)
a = int(input())
b = 5
multiple(a, b)
