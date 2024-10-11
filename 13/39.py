from ipaddress import ip_address, ip_network

ip = ip_address('93.138.164.49')

for mask in range(32): 
    net = ip_network(f'{ip}/{mask}', 0)
    # if '93.138.160.0' in str(net): 
    #     print(net)
    print(net)
