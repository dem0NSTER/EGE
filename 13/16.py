from ipaddress import ip_address, ip_network

ip = ip_address('154.201.208.17')

for mask in range(31): 
    net = ip_network(f'{ip}/{mask}', 0)
    if '154.201.192.0' in str(net) and net[0] < ip < net[-1]: 
        print(net, net.netmask)