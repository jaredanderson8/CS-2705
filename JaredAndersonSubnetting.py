#CS2705
#IPv4 Address Manipulation
#Jared Anderson

import ipaddress

#question 1
print("What is the subnet mask value for:")
#1
ipInterface = ipaddress.ip_interface('192.168.1.2/2')
print("/t 1. 2-bit mask: {}".format(ipInterface.netmask))
#2
ipInterface = ipaddress.ip_interface('192.168.1.2/13')
print("/t 2. 13-bit mask: {}".format(ipInterface.netmask))
#3
ipInterface = ipaddress.ip_interface('192.168.1.2/5')
print("/t 3. 5-bit mask: {}".format(ipInterface.netmask))
#4
ipInterface = ipaddress.ip_interface('192.168.1.2/11')
print("/t 4. 11-bit mask: {}".format(ipInterface.netmask))
#5
ipInterface = ipaddress.ip_interface('192.168.1.2/9')
print("/t 5. 9-bit mask: {}".format(ipInterface.netmask))
#6
ipInterface = ipaddress.ip_interface('192.168.1.2/10')
print("/t 6. 10-bit mask: {}".format(ipInterface.netmask))
#7
ipInterface = ipaddress.ip_interface('192.168.1.2/4')
print("/t 7. 4-bit mask: {}".format(ipInterface.netmask))
#8
ipInterface = ipaddress.ip_interface('192.168.1.2/14')
print("/t 8. 14-bit mask: {}".format(ipInterface.netmask))
#9
ipInterface = ipaddress.ip_interface('192.168.1.2/6')
print("/t 9. 6-bit mask: {}".format(ipInterface.netmask))
#10
ipInterface = ipaddress.ip_interface('192.168.1.2/8')
print("/t 10. 8-bit mask: {}".format(ipInterface.netmask))
#11
ipInterface = ipaddress.ip_interface('192.168.1.2/12')
print("/t 11. 12-bit mask: {}".format(ipInterface.netmask))

#question 2
ipInterface = ipaddress.ip_interface('132.8.150.67/22')
ipNetwork = ipInterface.network
print("\n2. Given 132.8.150.67/22, find the following")
print("\tNetwork address is: {}".format((ipNetwork).network_address))
print("\tBroadcast address is: {}".format((ipNetwork).broadcast_address))
print("\tNumber of host addresses: {}".format(len(list(ipNetwork.hosts()))))
print("\tValid host address range: {0} - {1}".format((((ipNetwork).network_address)+1), (((ipNetwork).broadcast_address)-1)))

#question 3
ipInterface = ipaddress.ip_interface('200.16.5.74/30')
ipNetwork = ipInterface.network
print("\n3. Given 200.16.5.74/30 , find the following")
print("\tNetwork address is: {}".format((ipNetwork).network_address))
print("\tBroadcast address is: {}".format((ipNetwork).broadcast_address))
print("\tNumber of host addresses: {}".format(len(list(ipNetwork.hosts()))))
print("\tValid host address range: {0} - {1}".format((((ipNetwork).network_address)+1), (((ipNetwork).broadcast_address)-1)))

#question 4
ipInterface = ipaddress.ip_interface('166.0.13.8/22')
ipNetwork = ipInterface.network
print("\n4. Given 200.16.5.74 with subnet mask of 255.255.252.0, find the following")
print("\tNetwork address is: {}".format((ipNetwork).network_address))
print("\tBroadcast address is: {}".format((ipNetwork).broadcast_address))
print("\tNumber of host addresses: {}".format(len(list(ipNetwork.hosts()))))
print("\tValid host address range: {0} - {1}".format((((ipNetwork).network_address)+1), (((ipNetwork).broadcast_address)-1)))

#question 5
ipInterface = ipaddress.ip_interface('255.255.240.0')
ipNetwork = ipInterface.network
print("\n5. With a subnet mask of 255.255.252.0, find the following")
print("\tNumber of bits in the subnet mask: {}".format((ipNetwork).prefixlen))
print("\tNumber of hosts: {}".format(len(list((ipNetwork).hosts()))))

#question 6
ipInterface = ipaddress.ip_interface('255.255.255.192')
ipNetwork = ipInterface.network
print("\n6. With a subnet mask of 255.255.255.192, find the following")
print("\tNumber of bits in the subnet mask: {}".format((ipNetwork).prefixlen))
print("\tNumber of hosts: {}".format(len(list((ipNetwork).hosts()))))

#question 7
ipInterface = ipaddress.ip_interface('255.255.252.0')
ipNetwork = ipInterface.network
print("\n7. With a subnet mask of 255.255.252.0, find the following")
print("\tNumber of bits in the subnet mask: {}".format((ipNetwork).prefixlen))
print("\tNumber of hosts: {}".format(len(list((ipNetwork).hosts()))))

#question 8
ipInterface = ipaddress.ip_interface('255.255.255.248')
ipNetwork = ipInterface.network
print("\n8. With a subnet mask of 255.255.255.248, find the following")
print("\tNumber of bits in the subnet mask: {}".format((ipNetwork).prefixlen))
print("\tNumber of hosts: {}".format(len(list((ipNetwork).hosts()))))

#9
print("\nYou’re a manager of a network that has 56 remote site and you have one Class B license. What subnet mask would you use with having the max amount of hosts at each site 1000?")
ipInterface = ipaddress.ip_interface('10.10.10.10/16')
ipNetwork = ipInterface.network
bitsBorrowed = 7
ipSubnetLength = ipNetwork.prefixlen + bitsBorrowed
print("The subnet mask length is: {}".format(ipSubnetLength))
print("The {0} subnets are less than the {1} subnets that were created".format((ipSubnetLength), len(list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff=(bitsBorrowed))))))
ipSubnet = str('10.10.10.10/') + str(ipSubnetLength)
ipSubnetAddress = ipaddress.ip_network(ipSubnet, strict=False)
print('The 1000 addresses needed are equal to or less than the {} hosts in each subnet.'.format(len(list(ipaddress.ip_network(ipSubnetAddress).hosts()))))
