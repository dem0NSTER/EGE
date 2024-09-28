from ipaddress import ip_network
c = 0

for i in range(33): 
    net = ip_network(f'175.122.80.13/{i}', 0)
    if net.num_addresses >= 60 and '175.122.80.0' in str(net): 
        c += 1
        print(net, c)