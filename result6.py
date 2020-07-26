print("Please Enter A Year")
year = input()
if (year % 400 == 0):
	print (str(int(year))+ " is a leap year!" );
elif (year % 100 == 0):
	print (str(int(year))+ " is not a leap year!");
elif (year %4 == 0):
	print (str(int(year))+ " is a leap year!");
else:
	print (str(int(year))+ " is not a leap year!");



