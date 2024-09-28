from ipaddress import ip_address, ip_network

ip = ip_address('122.21.49.91')

for mask in range(31): 
    net = ip_network(f'{ip}/{mask}', 0)
    if '122.21.48.0' in str(net) and net[0] < ip < net[-1]: 
        print(net)