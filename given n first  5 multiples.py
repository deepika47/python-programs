n = int(input())
x=[]
if(n>0):
    for i in range(1,6):
       x.append(n*i)
else:
    print("negative input")
print(*x,sep=' ')

