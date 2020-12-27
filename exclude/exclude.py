from netaddr import *
import os
import sys,getopt

def args(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"he:f:",["ifile=","ofile="])
      #print (opts,args)
   except getopt.GetoptError:
      print ('exclude.py -e <excludelist> -o <fromlist>')
      sys.exit(2)
      exit()
   if opts == []:
         print ('exclude.py -e <excludelist> -o <fromlist>')
         exit()
   for opt, arg in opts:
      if opt == '-h':
         print ('exclude.py -e <excludelist> -o <fromlist>')
         sys.exit()
      elif opt in ("-e", "--ifile"):
        file2 = arg
      elif opt in ("-f", "--ofile"):
        file1 = arg
   #print ('Input file is ', inputfile)
   #print ('Output file is ', outputfile)
   return (file1,file2)


#[inputfile, outputfile] = args(sys.argv[1:])


def read_files(file1,file2):
    fileName1 = file1
    with open(os.path.join(sys.path[0], fileName1), 'r') as f:
        ranges = f.read().splitlines()

    fileName2=file2
    with open(os.path.join(sys.path[0], fileName2), 'r') as g:
        exclude = g.read().splitlines()
    return (ranges,exclude)

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


[file1, file2] = args(sys.argv[1:])
[ranges,exclude] = read_files(file1,file2)
ip_range = range_to_single(ip_ranges=ranges)

dup_list = range_to_single (ip_ranges=exclude)

for item in dup_list:
    ip_range = remove_dup(ip_range,item)
    
x = cidr_merge(ip_range)
file = open('output.txt','w') 
for ip in x:
    print (ip)
    file.write(f"{str(ip)}\n")
file.close()


