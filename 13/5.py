from ipaddress import ip_network

for i in range(33): 
    net1 = ip_network(f'112.117.107.70/{i}', 0)
    net2 = ip_network(f'112.117.121.80/{i}', 0)
    if net1 == net2: 
        print(net1, net1.netmask)