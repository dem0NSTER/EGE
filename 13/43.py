from ipaddress import ip_network, ip_address

net = ip_network('172.16.128.0/255.255.192.0')

c = 0
for ip in net: 
    bin_ip = bin(int(ip))[2:].zfill(32)

    if bin_ip.count('1') % 2 != 0: 
        c += 1

print(c)
