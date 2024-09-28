from ipaddress import ip_network

for i in range(33): 
    net1 = ip_network(f'157.127.182.76/{i}', 0)
    net2 = ip_network(f'157.127.190.80/{i}', 0)
    if net1 != net2: 
        print(i)