#jared anderson cs2705
#convert IP addresses programmatically

#************************decimal to binary*******************************
print("Converting from decimal to binary: \n")
#convert 192.168.3.6 to binary
octet01=192
octet02=168
octet03=3
octet04=6

binoctet01=bin(octet01) [2:].zfill(8)
binoctet02=bin(octet02) [2:].zfill(8)
binoctet03=bin(octet03) [2:].zfill(8)
binoctet04=bin(octet04) [2:].zfill(8)

IPAddress=("IP address: {0}.{1}.{2}.{3}") 
print(IPAddress.format(octet01,octet02,octet03,octet04))

IPAddress=("The converted IP address is: {0}.{1}.{2}.{3} \n") 
print(IPAddress.format(binoctet01,binoctet02,binoctet03,binoctet04))

#convert 172.168.200.253 to binary
octet01=172
octet02=168
octet03=200
octet04=253

binoctet01=bin(octet01) [2:].zfill(8)
binoctet02=bin(octet02) [2:].zfill(8)
binoctet03=bin(octet03) [2:].zfill(8)
binoctet04=bin(octet04) [2:].zfill(8)

IPAddress=("IP address: {0}.{1}.{2}.{3}") 
print(IPAddress.format(octet01,octet02,octet03,octet04))

IPAddress=("The converted IP address is: {0}.{1}.{2}.{3} \n")
print(IPAddress.format(binoctet01,binoctet02,binoctet03,binoctet04))

#convert 10.200.42.93 to binary
octet01=10
octet02=200
octet03=42
octet04=93

binoctet01=bin(octet01) [2:].zfill(8)
binoctet02=bin(octet02) [2:].zfill(8)
binoctet03=bin(octet03) [2:].zfill(8)
binoctet04=bin(octet04) [2:].zfill(8)

IPAddress=("IP address: {0}.{1}.{2}.{3}") 
print(IPAddress.format(octet01,octet02,octet03,octet04))

IPAddress=("The converted IP address is: {0}.{1}.{2}.{3} \n")
print(IPAddress.format(binoctet01,binoctet02,binoctet03,binoctet04))

#convert 21.12.198.2 to binary
octet01=21
octet02=12
octet03=198
octet04=2

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

#convert 01101100.11001100.00110000.11001100 to decimal
octet01='01101100'
octet02='11101011'
octet03='11001100'
octet04='11001100'

decoctet01=int(octet01, 2)
decoctet02=int(octet02, 2) 
decoctet03=int(octet03, 2) 
decoctet04=int(octet04, 2) 

IPAddress=("IP address: {0}.{1}.{2}.{3}") 
print(IPAddress.format(octet01,octet02,octet03,octet04))

IPAddress=("The converted IP address is: {0}.{1}.{2}.{3} \n")
print(IPAddress.format(decoctet01,decoctet02,decoctet03,decoctet04))

#convert 01010110.10100011.11001111.11111111 to decimal
octet01='01010110'
octet02='10100011'
octet03='11001111'
octet04='11111111'

decoctet01=int(octet01, 2)
decoctet02=int(octet02, 2) 
decoctet03=int(octet03, 2) 
decoctet04=int(octet04, 2) 

IPAddress=("IP address: {0}.{1}.{2}.{3}") 
print(IPAddress.format(octet01,octet02,octet03,octet04))

IPAddress=("The converted IP address is: {0}.{1}.{2}.{3} \n")
print(IPAddress.format(decoctet01,decoctet02,decoctet03,decoctet04))

#convert 00001001.10101010.11111110.11100011 to decimal
octet01='00001001'
octet02='10101010'
octet03='11111110'
octet04='11100011'

decoctet01=int(octet01, 2)
decoctet02=int(octet02, 2) 
decoctet03=int(octet03, 2) 
decoctet04=int(octet04, 2) 

IPAddress=("IP address: {0}.{1}.{2}.{3}") 
print(IPAddress.format(octet01,octet02,octet03,octet04))

IPAddress=("The converted IP address is: {0}.{1}.{2}.{3} \n")
print(IPAddress.format(decoctet01,decoctet02,decoctet03,decoctet04))

#convert 10101010.01101100.11111100.01110011 to decimal
octet01='10101010'
octet02='01101100'
octet03='11111100'
octet04='01110011'

decoctet01=int(octet01, 2)
decoctet02=int(octet02, 2) 
decoctet03=int(octet03, 2) 
decoctet04=int(octet04, 2) 

IPAddress=("IP address: {0}.{1}.{2}.{3}") 
print(IPAddress.format(octet01,octet02,octet03,octet04))

IPAddress=("The converted IP address is: {0}.{1}.{2}.{3} \n")
print(IPAddress.format(decoctet01,decoctet02,decoctet03,decoctet04))