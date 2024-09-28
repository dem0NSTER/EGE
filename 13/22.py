from ipaddress import ip_network

for mask in range(33): 
    net = ip_network(f'165.112.200.70/{mask}', 0)
    net2 = ip_network(f'165.112.175.80/{mask}', 0)
    if net == net2:
        print(net) 