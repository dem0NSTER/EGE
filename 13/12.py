from ipaddress import ip_network

net = ip_network('211.48.136.64/255.255.255.224')
c = 0

for ip in net: 
    binip = f'{ip:b}'
    # bin2 = bin(int(ip))[2::].zfill(32)
    if binip[-2:] == '11': 
        c += 1

print(c)
