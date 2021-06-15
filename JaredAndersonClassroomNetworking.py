#CS2705
#Classroom networking with python
#Jared Anderson

import ipaddress

#Classroom 1 – 30 computers and printers --32 addresses
#Classroom 2 – 30 computers and printers --32 addresses
#Classroom 3 – 14 computers --16 addresses
#Classroom 4 – 14 computers --16 addresses
#Classroom 5 – 14 computers --16 addresses
#Lab 1 – 6 computers --8 addresses
#Lab 2 – 6 computers --8 addresses

#Given address space is 138.191.0.0/25
ipInterface = ipaddress.ip_interface('138.191.0.0/25')
ipNetwork = ipInterface.network

classroom = (list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff=2)))

#print("--Subnets--")
#print(classroom[0]) #classroom 1
#print(classroom[1]) #classroom 2
#print(classroom[2]) #classrooms 3 and 4
#print(classroom[3]) #classroom 5 and labs 1 and 2

smallClass1 = (list(ipaddress.ip_network(classroom[2]).subnets()))
smallClass2 = (list(ipaddress.ip_network(classroom[3]).subnets()))

#print("\n--divided classrooom subnets--")
#print(smallClass1[0]) #classroom 3
#print(smallClass1[1]) #classroom 4
#print(smallClass2[0]) #classroom 5
#print(smallClass2[1]) #labs 1 and 2

labs = (list(ipaddress.ip_network(smallClass2[1]).subnets()))

#print("\n--divided lab subnets--")
#print(labs[0]) #lab 1
#print(labs[1]) #lab 2

print("Assignments information in longest mask order:")
#print("30 networks:")
print("\t Network Name: Lab 1")
print("\t Prefix Length: {}".format((labs[0]).prefixlen))
print("\t Network Address: {}".format((labs[0]).network_address))
print("\t Broadcast Address: {}".format((labs[0]).broadcast_address))
print("\t Number of Hosts {}".format(len(list((labs[0]).hosts()))))
print("\t Valid Host Range: {} - {}".format((((labs[0]).network_address)+1),((labs[0]).broadcast_address)-1))
print()
print("\t Network Name: Lab 2")
print("\t Prefix Length: {}".format((labs[1]).prefixlen))
print("\t Network Address: {}".format((labs[1]).network_address))
print("\t Broadcast Address: {}".format((labs[1]).broadcast_address))
print("\t Number of Hosts {}".format(len(list((labs[1]).hosts()))))
print("\t Valid Host Range: {} - {}".format((((labs[1]).network_address)+1),((labs[1]).broadcast_address)-1))
print()
print("\t Network Name: Classroom 3")
print("\t Prefix Length: {}".format((smallClass1[0]).prefixlen))
print("\t Network Address: {}".format((smallClass1[0]).network_address))
print("\t Broadcast Address: {}".format((smallClass1[0]).broadcast_address))
print("\t Number of Hosts {}".format(len(list((smallClass1[0]).hosts()))))
print("\t Valid Host Range: {} - {}".format((((smallClass1[0]).network_address)+1),((smallClass1[0]).broadcast_address)-1))
print()
print("\t Network Name: Classroom 4")
print("\t Prefix Length: {}".format((smallClass1[1]).prefixlen))
print("\t Network Address: {}".format((smallClass1[1]).network_address))
print("\t Broadcast Address: {}".format((smallClass1[1]).broadcast_address))
print("\t Number of Hosts {}".format(len(list((smallClass1[1]).hosts()))))
print("\t Valid Host Range: {} - {}".format((((smallClass1[1]).network_address)+1),((smallClass1[1]).broadcast_address)-1))
print()
print("\t Network Name: Classroom 5")
print("\t Prefix Length: {}".format((smallClass2[0]).prefixlen))
print("\t Network Address: {}".format((smallClass2[0]).network_address))
print("\t Broadcast Address: {}".format((smallClass2[0]).broadcast_address))
print("\t Number of Hosts {}".format(len(list((smallClass2[0]).hosts()))))
print("\t Valid Host Range: {} - {}".format((((smallClass2[0]).network_address)+1),((smallClass2[0]).broadcast_address)-1))
print()
print("\t Network Name: Classroom 1")
print("\t Prefix Length: {}".format((classroom[0]).prefixlen))
print("\t Network Address: {}".format((classroom[0]).network_address))
print("\t Broadcast Address: {}".format((classroom[0]).broadcast_address))
print("\t Number of Hosts {}".format(len(list((classroom[0]).hosts()))))
print("\t Valid Host Range: {} - {}".format((((classroom[0]).network_address)+1),((classroom[0]).broadcast_address)-1))
print()
print("\t Network Name: Classroom 2")
print("\t Prefix Length: {}".format((classroom[1]).prefixlen))
print("\t Network Address: {}".format((classroom[1]).network_address))
print("\t Broadcast Address: {}".format((classroom[1]).broadcast_address))
print("\t Number of Hosts {}".format(len(list((classroom[1]).hosts()))))
print("\t Valid Host Range: {} - {}".format((((classroom[1]).network_address)+1),((classroom[1]).broadcast_address)-1))
print()
