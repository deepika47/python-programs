N = int(input())
m = list(map(int,input().split()))[:N]
print(*sorted(m), sep=' ')
