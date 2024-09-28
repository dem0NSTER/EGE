from ipaddress import ip_network

net = ip_network('184.178.54.144/255.255.255.240')
c = 0

for ip in net: 
    ip_parts = [int(i) for i in str(ip).split('.')]
    bin_ip_parts = [bin(i)[2:] for i in ip_parts]
    bin_ip = '.'.join(bin_ip_parts)
    if bin_ip.count('111') != 0: 
        c += 1

print(c)