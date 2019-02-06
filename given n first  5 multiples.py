n = int(input())
a=[]
if(n>0):
    for i in range(1,6):
       a.append(n*i)
       
else:
    print("negative input")
    
print(*a,sep=' ')

