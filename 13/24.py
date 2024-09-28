from ipaddress import ip_network
c = 0

net = ip_network('192.168.240.0/255.255.255.0')
for ip in net: 
    bin_ip = bin(int(ip))[2:].zfill(32)
    if bin_ip.count('1') == bin_ip.count('0'): 
        c += 1
print(c)