from ipaddress import ip_network
c = 0

for i in range(33): 
    net = ip_network(f'76.155.48.2/{i}', 0)
    if '76.155.48.0' in str(net): 
        c += 1
        print(net, c)