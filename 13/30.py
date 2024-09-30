from ipaddress import ip_network, ip_address 

ip = ip_address('208.172.216.35')

for i in range(31): 
    net = ip_network(f'{ip}/{i}', 0)
    if '208.172.216.0' in str(net) and net[0] < ip < net[-1]: 
        print(net, net.num_addresses)