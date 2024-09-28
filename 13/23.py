from ipaddress import ip_network

for i in range(33): 
    net1 = ip_network(f'10.96.180.231/{i}', 0)
    net2 = ip_network(f'10.96.140.118/{i}', 0)
    if net1 != net2: 
        print(net1, net2)