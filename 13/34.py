from ipaddress import ip_address, ip_network

ip = ip_address('245.166.144.200')

for mask in range(32): 
    net = ip_network(f'{ip}/{mask}', 0)
    if '240.0.0.0' in str(net) and net[0] < ip < net[-1]: 
        print(net, net.netmask)