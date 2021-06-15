#jared anderson cs2705
#convert binary numbers programmatically

#************************decimal to binary*******************************
print("Converting from decimal to binary: \n")
#convert 192.168.16.13 to binary
octet01=192
octet02=168
octet03=16
octet04=38

binoctet01=bin(octet01) [2:].zfill(8)
binoctet02=bin(octet02) [2:].zfill(8)
binoctet03=bin(octet03) [2:].zfill(8)
binoctet04=bin(octet04) [2:].zfill(8)

IPAddress=("IP address: {0}.{1}.{2}.{3}") 
print(IPAddress.format(octet01,octet02,octet03,octet04))

IPAddress=("The converted IP address is: {0}.{1}.{2}.{3} \n") 
print(IPAddress.format(binoctet01,binoctet02,binoctet03,binoctet04))

#convert 164.10.241.2 to binary
octet01=164
octet02=110
octet03=241
octet04=2

binoctet01=bin(octet01) [2:].zfill(8)
binoctet02=bin(octet02) [2:].zfill(8)
binoctet03=bin(octet03) [2:].zfill(8)
binoctet04=bin(octet04) [2:].zfill(8)

IPAddress=("IP address: {0}.{1}.{2}.{3}") 
print(IPAddress.format(octet01,octet02,octet03,octet04))

IPAddress=("The converted IP address is: {0}.{1}.{2}.{3} \n")
print(IPAddress.format(binoctet01,binoctet02,binoctet03,binoctet04))

#convert 10.244.116.15 to binary
octet01=10
octet02=244
octet03=116
octet04=12

binoctet01=bin(octet01) [2:].zfill(8)
binoctet02=bin(octet02) [2:].zfill(8)
binoctet03=bin(octet03) [2:].zfill(8)
binoctet04=bin(octet04) [2:].zfill(8)

IPAddress=("IP address: {0}.{1}.{2}.{3}") 
print(IPAddress.format(octet01,octet02,octet03,octet04))

IPAddress=("The converted IP address is: {0}.{1}.{2}.{3} \n")
print(IPAddress.format(binoctet01,binoctet02,binoctet03,binoctet04))

#convert 15.255.200.153 to binary
octet01=15
octet02=255
octet03=200
octet04=153

binoctet01=bin(octet01) [2:].zfill(8)
binoctet02=bin(octet02) [2:].zfill(8)
binoctet03=bin(octet03) [2:].zfill(8)
binoctet04=bin(octet04) [2:].zfill(8)

IPAddress=("IP address: {0}.{1}.{2}.{3}") 
print(IPAddress.format(octet01,octet02,octet03,octet04))

IPAddress=("The converted IP address is: {0}.{1}.{2}.{3} \n")
print(IPAddress.format(binoctet01,binoctet02,binoctet03,binoctet04))

#convert 172.99.62.9 to binary
octet01=172
octet02=99
octet03=62
octet04=9

binoctet01=bin(octet01) [2:].zfill(8)
binoctet02=bin(octet02) [2:].zfill(8)
binoctet03=bin(octet03) [2:].zfill(8)
binoctet04=bin(octet04) [2:].zfill(8)

IPAddress=("IP address: {0}.{1}.{2}.{3}") 
print(IPAddress.format(octet01,octet02,octet03,octet04))

IPAddress=("The converted IP address is: {0}.{1}.{2}.{3} \n")
print(IPAddress.format(binoctet01,binoctet02,binoctet03,binoctet04))

#***********************binary to decimal*********************************
print("Converting from binary to decimal: \n")

#convert 10110100.11101011.00001000.10010001 to decimal
octet01='10110100'
octet02='11101011'
octet03='00001000'
octet04='10010001'

decoctet01=int(octet01, 2)
decoctet02=int(octet02, 2) 
decoctet03=int(octet03, 2) 
decoctet04=int(octet04, 2) 

IPAddress=("IP address: {0}.{1}.{2}.{3}") 
print(IPAddress.format(octet01,octet02,octet03,octet04))

IPAddress=("The converted IP address is: {0}.{1}.{2}.{3} \n")
print(IPAddress.format(decoctet01,decoctet02,decoctet03,decoctet04))

#convert 10001100.11111111.11000000.00000001 to decimal
octet01='10001100'
octet02='11111111'
octet03='11000000'
octet04='00000001'

decoctet01=int(octet01, 2)
decoctet02=int(octet02, 2) 
decoctet03=int(octet03, 2) 
decoctet04=int(octet04, 2) 

IPAddress=("IP address: {0}.{1}.{2}.{3}") 
print(IPAddress.format(octet01,octet02,octet03,octet04))

IPAddress=("The converted IP address is: {0}.{1}.{2}.{3} \n")
print(IPAddress.format(decoctet01,decoctet02,decoctet03,decoctet04))

#convert 00010001.11001100.00000001.00010010 to decimal
octet01='00010001'
octet02='11001100'
octet03='00000001'
octet04='00010010'

decoctet01=int(octet01, 2)
decoctet02=int(octet02, 2) 
decoctet03=int(octet03, 2) 
decoctet04=int(octet04, 2) 

IPAddress=("IP address: {0}.{1}.{2}.{3}") 
print(IPAddress.format(octet01,octet02,octet03,octet04))

IPAddress=("The converted IP address is: {0}.{1}.{2}.{3} \n")
print(IPAddress.format(decoctet01,decoctet02,decoctet03,decoctet04))

#convert 11100111.00110011.10101010.11111110 to decimal
octet01='11100111'
octet02='00110011'
octet03='10101010'
octet04='11111110'

decoctet01=int(octet01, 2)
decoctet02=int(octet02, 2) 
decoctet03=int(octet03, 2) 
decoctet04=int(octet04, 2) 

IPAddress=("IP address: {0}.{1}.{2}.{3}") 
print(IPAddress.format(octet01,octet02,octet03,octet04))

IPAddress=("The converted IP address is: {0}.{1}.{2}.{3} \n")
print(IPAddress.format(decoctet01,decoctet02,decoctet03,decoctet04))

#convert 00010111.11101110.01010101.10000000 to decimal
octet01='00010111'
octet02='11101110'
octet03='01010101'
octet04='10000000'

decoctet01=int(octet01, 2)
decoctet02=int(octet02, 2) 
decoctet03=int(octet03, 2) 
decoctet04=int(octet04, 2) 

IPAddress=("IP address: {0}.{1}.{2}.{3}") 
print(IPAddress.format(octet01,octet02,octet03,octet04))

IPAddress=("The converted IP address is: {0}.{1}.{2}.{3} \n")
print(IPAddress.format(decoctet01,decoctet02,decoctet03,decoctet04))