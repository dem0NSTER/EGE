from ipaddress import ip_address, ip_network

ip = ip_address('119.167.50.77')

for i in range(31): 
    net = ip_network(f'{ip}/{i}', 0)
    if '119.167.48.0' in str(net) and net[0] < ip < net[-1]: 
        print(net, net.netmask)