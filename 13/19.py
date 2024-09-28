from ipaddress import ip_address, ip_network

ip = ip_address('158.116.11.146')
c = 0

for mask in range(32): 
    net = ip_network(f'{ip}/{mask}', 0)
    if '158.116.0.0' in str(net) and net[0] < ip < net[-1]: 
        c += 1

print(c)