#point 1 in project--- date modified: 2016-02-25 
#Sarah McComas

import sys                          #to use for sys.argv[]
script_name= sys.argv[0]
input_file = sys.argv[1]            # so that you can only write 'python point1new.py input_file_name'
#output_file= sys.argv[2]
f=open(input_file)                  #need to open the input file
aa=f.read().splitlines()            #splitting to read line by line, will need in aa

header= "######'A':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'K':9, 'L':10, 'M':11,\
'N':12, 'P':13, 'Q':14, 'R':15, 'S':16, 'T':17, 'Y':18, 'V':19, 'W':20"
print header

name= []                    #should print the first name as it looks like in fasta
seq= []                   #will hold the list of the amino acids
struct= []                 #will hold a list of the structure values
numbs= []                    #will use to convert struct letters to numbers
target=[]                   #will use to print -1 or 1 for the target values. I THINK this is right. Should be -1 for all non M's

amino= {'A':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'K':9, 'L':10, 'M':11,\
'N':12, 'P':13, 'Q':14, 'R':15, 'S':16, 'T':17, 'Y':18, 'V':19, 'W':20}


for line in aa:
	if '>' in line:
		name.append(line)     #making a list of all fasta format names
	elif 'O' not in line:
		seq.append(line)       #making a list of amino acids by letter name
	else:
		struct.append(line)
		

for struct_string in struct:      
	for single_struct in struct_string:               #otherwise python evaluated 'IOOOMMMMOOOOOIII' as one entity and obviously that does not == "M"
		if single_struct=='M':
			numbs.append(1)
			target.append(1)
		else:
			numbs.append(0)
			target.append (-1)
print numbs
print target


zippy= zip(seq, numbs)
for a, b in zippy:
	print zippy

        #r.append(f)

