import statistics
N = int(input())
m = list(map(int,input().split()))[:N]
k = sorted(m)
print(statistics.median(k))
