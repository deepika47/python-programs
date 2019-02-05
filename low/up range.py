low=int(input("Enter the lower limit for the range:"))
up=int(input("Enter the upper limit for the range:"))
for i in range(low,up+1):
    if(i%2!=0):
        print(i)
