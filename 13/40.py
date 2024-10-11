from ipaddress import ip_network

net = ip_network('0.0.0.0/255.255.255.224')

print(net.num_addresses)