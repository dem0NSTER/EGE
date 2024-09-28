from ipaddress import ip_network

for i in range(33): 
    net = ip_network(f'148.195.140.28/{i}', 0)
    if '148.195.140.0' in str(net): 
        print(net)