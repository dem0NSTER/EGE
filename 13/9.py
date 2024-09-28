from ipaddress import ip_network


for i in range(33): 
    net = ip_network(f'108.133.75.91/{i}', 0)
    if '108.133.75.64' in str(net): 
        print(net, net.num_addresses)
