#CS2705
#IPv4 Address Manipulation
#Jared Anderson

import ipaddress

#question 1
ipInterface = ipaddress.ip_interface('192.168.2.76/28')
ipNetwork = ipInterface.network

print("\n1. What is the first address of a block of classless addresses if one of the addresses is 192.168.2.76/28?")
print("Network address is: {}".format((ipaddress.ip_network(ipNetwork).network_address)))
print("The first usable address is: {}".format((ipaddress.ip_network(ipNetwork).network_address)+1))

#question 2
ipInterface = ipaddress.ip_interface('192.168.2.76/9')
ipNetwork = ipInterface.network

print("\n2. What is the first address of a block of classless addresses if one of the addresses is 192.168.2.76/9?")
print("Network address is: {}".format((ipaddress.ip_network(ipNetwork).network_address)))
print("The first usable address is: {}".format((ipaddress.ip_network(ipNetwork).network_address)+1))

#question 3
ipInterface = ipaddress.ip_interface('192.168.2.137/27')
ipNetwork = ipInterface.network

print("\n3. What is the first address of a block of classless addresses if one of the addresses is 192.168.2.137/27?")
print("Network address is: {}".format((ipaddress.ip_network(ipNetwork).network_address)))
print("The first usable address is: {}".format((ipaddress.ip_network(ipNetwork).network_address)+1))

#question 4
ipInterface = ipaddress.ip_interface('101.10.2.8/15')
ipNetwork = ipInterface.network

print("\n4. Find the number of addresses in a block of classless addresses if one of the addresses is 101.10.2.8/15.")
print("The total number of addresses in this subnet is: {}".format(ipaddress.ip_network(ipNetwork).num_addresses))
print("The number of usable addresses in this subnet is: {}".format((ipaddress.ip_network(ipNetwork).num_addresses)-2))

#question 5
ipInterface = ipaddress.ip_interface('101.10.2.8/29')
ipNetwork = ipInterface.network

print("\n5. Find the number of addresses in a block of classless addresses if one of the addresses is 101.10.2.8/29.")
print("The total number of addresses in this subnet is: {}".format(ipaddress.ip_network(ipNetwork).num_addresses))
print("The number of usable addresses in this subnet is: {}".format((ipaddress.ip_network(ipNetwork).num_addresses)-2))

#question 6
ipInterface = ipaddress.ip_interface('192.168.2.137/27')
ipNetwork = ipInterface.network

print("\n6. What is the last address of a block of classless addresses if one of the addresses is 192.168.2.137/27?")
print("Broadcast address is: {}".format(ipaddress.ip_network(ipNetwork).broadcast_address))
print("The last usable address is: {}".format((ipaddress.ip_network(ipNetwork).broadcast_address)-1))

#question 7
ipInterface = ipaddress.ip_interface('110.10.2.55/30')
ipNetwork = ipInterface.network

print("\n7. What is the last address of a block of classless addresses if one of the addresses is 110.10.2.55/30?")
print("Broadcast address is: {}".format(ipaddress.ip_network(ipNetwork).broadcast_address))
print("The last usable address is: {}".format((ipaddress.ip_network(ipNetwork).broadcast_address)-1))

#question 8
ipInterface = ipaddress.ip_interface('110.10.10.64/20')
ipNetwork = ipInterface.network

print("\n8. An organization is granted a block; one address is 110.10.10.64/20. The organization needs ten subnets. What is the subnet prefix length?")
print("List of 16 subnets: {}".format(list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff=4))))
print("The subnet prefix length is /24.")

#question 9
ipInterface = ipaddress.ip_interface('110.10.10.64/25')
ipNetwork = ipInterface.network

print("\n9. An organization is granted a block; one address is 110.10.10.64/25. If the subnet prefix length is /28, what is the maximum number of subnets?")
print("List of 8 subnets: {}".format(list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff=3))))
print("8 subnets with 16 addresses in each subnet.")

#question 10
ipInterface = ipaddress.ip_interface('156.78.51.24/25')
ipNetwork = ipInterface.network

print("\n10. An organization is granted a block of classless addresses with the starting address: 156.78.51.24/25. How many addresses are granted?")
print("The total number of addresses in this subnet is: {}".format(ipaddress.ip_network(ipNetwork).num_addresses))

#question 11
ipInterface = ipaddress.ip_interface('156.78.51.24/30')
ipNetwork = ipInterface.network

print("\n11. An organization is granted a block of classless addresses with the starting address: 156.78.51.24/30. How many addresses are granted?")
print("The total number of addresses in this subnet is: {}".format(ipaddress.ip_network(ipNetwork).num_addresses))

#question 12
ipInterface = ipaddress.ip_interface('166.25.132.0/3')
ipNetwork = ipInterface.network

print("\n12. An organization is granted a block of classless addresses with the starting address: 166.25.132.0/3. How many addresses are granted?")
print("The total number of addresses in this subnet is: {}".format(ipaddress.ip_network(ipNetwork).num_addresses))

#question poop
ipInterface = ipaddress.ip_interface('192.168.20.5/24')
ipNetwork = ipInterface.network

print("\npoop. What is the last address of a block of classless addresses if one of the addresses is 110.10.2.55/30?")
print("Broadcast address is: {}".format(ipaddress.ip_network(ipNetwork).broadcast_address))
print("Network address is: {}".format((ipaddress.ip_network(ipNetwork).network_address)))