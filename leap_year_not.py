year = int(input("Please Enter any Year: "))

if (year%400 == 0):
          print("%d is a Leap Year" %year)
elif (year%100 == 0):
          print("%d is Not a  Leap Year" %year)
elif (year%4 == 0):
          print("%d is a Leap Year" %year)
else:
          print("%d is Not a Leap Year" %year)