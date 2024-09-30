from ipaddress import ip_network, ip_address

ip = ip_address('98.162.71.94')

for i in range(31):
    net = ip_network(f'98.162.71.94/{i}', 0)
    if '98.162.71.64' in str(net) and net[0] < ip < net[-1]: 
        print(net)