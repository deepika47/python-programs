n= int(input("enter number:"))
count = 0
while (n > 0):
  n = n//10
  count = count + 1
print ("Total number of digits : ",count)
