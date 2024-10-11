from ipaddress import ip_network

net = ip_network('200.135.210.135/255.255.248.0', 0)
print(net)
