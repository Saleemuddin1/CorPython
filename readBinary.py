bin1 = open ('leapYear.py',"rb")
for line in bin1:
	temp = "".join(str(ord(c)) + "," for c in list(line))
	print(temp)
