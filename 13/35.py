from ipaddress import ip_address, ip_network

ip = ip_address('106.184.0.0')
net = ip_network(f'{ip}/255.248.0.0')
c = 0

for i in net: 
    binip = bin(int(i))[2:].zfill(32)
    if binip.count('1') % 2 != 0: 
        c += 1
print(c)