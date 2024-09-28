from ipaddress import ip_network, ip_address

ip = ip_address('191.173.145.240')

for mask in range(33): 
    net = ip_network(f'{ip}/{mask}', 0)
    if '191.173.144.0' in str(net) and net[0] < ip < net[-1]: 
        print(net, net.num_addresses)