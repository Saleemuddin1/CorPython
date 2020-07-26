import binascii
with open ('/home/saleemuddin1/CorPy/leapYear.py','rb') as foo:
	vals = foo.read()
final =binascii.hexlify(vals)
with open ('/home/saleemuddin1/CorPy/result4.txt','rb') as fii:
	content2 = fii.read()
final2 =binascii.hexlify(content2)
final2 = final.decode("hex")
print("The contents of the Original File Are: ")
print(final2)
sparkles = open("result5.py","wb")
sparkles.write(final2)
sparkles.close()
print("The hex contents are also in file: result5.py")





