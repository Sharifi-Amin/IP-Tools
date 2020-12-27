from netaddr import *
import os
import sys



fileName='ips.txt'
with open(os.path.join(sys.path[0], fileName), 'r') as f:
    data = f.read().splitlines()



x = '192.168.0.0/24'
y = IPNetwork(x)
print (y)
range_list = []
for t in y:        
    range_list.append(IPNetwork(t))


    x = IPSet(range_list)
    single_ip_list = []
    for ip in x:
        
        #print(ip)
        single_ip_list.append(ip)
print(single_ip_list)