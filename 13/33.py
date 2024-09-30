from ipaddress import ip_address, ip_network

ip = ip_address('111.81.88.168')

for i in range(33): 
    net = ip_network(f'{ip}/{i}', 0)
    if '111.81.88.160' in str(net) and net[0] < ip < net[-1]: 
        print(net, net.netmask)