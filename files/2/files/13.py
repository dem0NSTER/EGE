from ipaddress import ip_network

# for i in range(9): 
#     s = '1' * i + '0' * (8 - i)
#     mask = int(s, 2)
#     net = ip_network(f'172.16.168.0/255.255.255.{mask}', 0)
    
#     c = 0
#     for ip in net: 
#         bin_ip = bin(int(ip))[2:].zfill(32)

#         if bin_ip.count('0') % 7 == 0: 
#             c += 1

#     if c == 35: 
#         print(mask)


net = ip_network(f'172.16.168.0/255.255.255.128', 0)
c = 0
for ip in net: 
    bin_ip = bin(int(ip))[2:].zfill(32)

    if bin_ip.count('0') % 7 == 0: 
        c += 1

print(c)
