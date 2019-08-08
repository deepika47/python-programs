def AP( A ,D,N) :
    sum = 0
    i = 0
    while i < N :
        sum = sum + A
        A = A + D
        i = i + 1
    return sum
N = int(input())
A = int(input())
D = int(input())
print (AP(A, D, N))
