from ipaddress import ip_network

for mask in range(33): 
    net = ip_network(f'111.81.208.27/{mask}', 0) 

    print(net, net.netmask)