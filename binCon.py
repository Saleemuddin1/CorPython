with open('/home/saleemuddin1/CorPy/leapYear.py', 'r') as txtfile:
    mytextstring = txtfile.read()
binarray = ' '.join(format(ch, 'b') for ch in bytearray(mytextstring))
with open('/home/saleemuddin1/CorPy/binary.bin', 'rb+') as binfile:
    binfile.write(binarray)
print ("Check File binary.bin for Output! ")
