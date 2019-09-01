x = []
count = 0
N = int(input())
for i in range (1,N+1):
    if (N % i==0):
          if (i % 2==0):
              count = count +1
              x.append(i)
if(count==0):
    print(N)
else:
    print(sep=" ",*x)
