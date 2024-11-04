from ipaddress import ip_network

net = ip_network('228.172.236.0/255.255.240.0', 0)

c = 0
for ip in net: 
    bin_ip = bin(int(ip))[2:].zfill(32)
    if bin_ip.count('1') % 5 != 0: 
        c += 1

print(c)
