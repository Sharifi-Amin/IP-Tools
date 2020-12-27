from netaddr import *
import os
import sys, getopt
def args(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
      #print (opts,args)
   except getopt.GetoptError:
      print ('merge.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
      exit()
   if opts == []:
         print ('merge.py -i <inputfile> -o <outputfile>')
         exit()
   for opt, arg in opts:
      if opt == '-h':
         print ('merge.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   #print ('Input file is ', inputfile)
   #print ('Output file is ', outputfile)
   return (inputfile,outputfile)


[inputfile, outputfile] = args(sys.argv[1:])


fileName= inputfile
with open(os.path.join(sys.path[0], fileName), 'r') as f:
    data = f.read().splitlines()


ip_list = [ip for ip in data]
merged = cidr_merge(ip_list)
f = open(outputfile, "w")


for ip_range in merged:
    print (ip_range)
    f.write(f'{ip_range}\n')

f.close()