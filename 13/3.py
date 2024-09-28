from ipaddress import ip_network

for i in range(32, 0, -1): 
    net = ip_network(f'241.185.253.57/{i}', 0)
    if '241.185.252.0' in str(net): 
        print(net)