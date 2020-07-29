bin1 = open ('/home/saleemuddin1/CorPy/leapYear.py',"rb")
for line in bin1:
	temp = "".join(str(ord(c)) + "," for c in list(line))
	print(temp)
