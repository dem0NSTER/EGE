from ipaddress import ip_network

net = ip_network('192.168.156.235/255.255.255.240', 0)
c = 0

for ip in net: 
    print(c, ip)
    c += 1
