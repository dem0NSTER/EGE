from ipaddress import ip_address, ip_network

ip = ip_address('128.175.95.31')
ip2 = ip_address('128.175.96.13')

for i in range(33): 
    net1 = ip_network(f'{ip}/{i}', 0)
    net2 = ip_network(f'{ip2}/{i}', 0)
    if net1 != net2: 
        print(net1, net1.netmask)