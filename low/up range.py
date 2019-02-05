low=int(input("Enter the lower limit value:"))
up=int(input("Enter the upper limit value:"))
for i in (low,up+1):
    if(i%2!=0):
        print(i)
