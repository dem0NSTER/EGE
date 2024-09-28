from ipaddress import ip_network, ip_address

ip = ip_address('118.193.30.139')

for i in range(32): 
    net = ip_network(f'118.193.30.139/{i}', 0)
    if '118.193.24.0' in str(net) and net[0] < ip < net[-1]: 
        print(net, net.netmask)