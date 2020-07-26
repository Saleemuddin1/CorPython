filer = open ('/home/saleemuddin1/CorPy/binary.bin','rb') 
byte = filer.read()
a = byte
b = a.split()
c = ""

for d in b:
	hello = int(d,2)
	fhi = chr(hello)
	c += fhi
print("The String Contents Are: ")
print (c)

filer2 = open('/home/saleemuddin1/CorPy/result6.py','w')
filer2.write(c)
filer2.close()
print("Also: The String Contents of binary.bin (Binary File) in File: result6.py")
	
	
	
		
