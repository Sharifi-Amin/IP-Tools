# IP-Tools
A collection of simple tools to merge, consolidate and mess around with CIDR subnets and IP ranges

## merge.py
Merge diffrent subnets, ranges and single IPs into the a the smallest list of subnets possible

```
Usage: merge.py -i \<inputfile\> -o \<outputfile\>
```

## exclude.py
exclude  a list of single IPs or a subnets from a bigger list of subnets or single IPs

```
Usage: exclude.py -e \<excludelist\> -f \<fromlist\>
```
