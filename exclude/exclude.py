from netaddr import *
import os
import sys,getopt

def args(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
      #print (opts,args)
   except getopt.GetoptError:
      print ('script.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
      exit()
   if opts == []:
         print ('script.py -i <inputfile> -o <outputfile>')
         exit()
   for opt, arg in opts:
      if opt == '-h':
         print ('script.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   #print ('Input file is ', inputfile)
   #print ('Output file is ', outputfile)
   return (inputfile,outputfile)


#[inputfile, outputfile] = args(sys.argv[1:])


fileName1='ranges.txt'
with open(os.path.join(sys.path[0], fileName1), 'r') as f:
    ranges = f.read().splitlines()

fileName2='remove.txt'
with open(os.path.join(sys.path[0], fileName2), 'r') as f:
    dup = f.read().splitlines()

def range_to_single(ip_ranges):
    range_list = []
    for ip_range in ip_ranges:        
        range_list.append(IPNetwork(ip_range))

    range_set = IPSet(range_list)
    single_ip_list = []
    for ip_range in range_list:
        for single_ip in range_set:
            #print(single_ip)
            single_ip_list.append(single_ip)
    return (single_ip_list)


def remove_dup(list,item):
    if item in list:
        list.remove(item)
        print(f'duplicate was found : {item}')
    return (list)



ip_range = range_to_single(ip_ranges=ranges)
#print(f'range: {ip_range}')
dup_list = range_to_single (ip_ranges=dup)
#print(f'dups: {dup_list}')
for item in dup_list:
    ip_range = remove_dup(ip_range,item)
#print(ip_range)    
x = cidr_merge(ip_range)
#print(x)
for ip in x:
    print (ip)
