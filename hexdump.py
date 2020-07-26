import binascii
with open ('/home/saleemuddin1/CorPy/leapYear.py','rb') as p:
	fin = p.read()
conclude =binascii.hexlify(fin)
print("The Hex Contents of leapYear.py Are: ")
print(conclude)
sparkly = open("/home/saleemuddin1/CorPy/result4.hex","w")
sparkly.write(conclude)
sparkly.close()
print("The hex contents are also in file: result4.hex")


