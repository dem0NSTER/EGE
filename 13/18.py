from ipaddress import ip_address, ip_network

ip = ip_address('173.103.25.118')

for mask in range(31): 
    net = ip_network(f'{ip}/{mask}', 0)
    if '173.103.24.0' in str(net) and net[0] < ip < net[-1]: 
        print(net)