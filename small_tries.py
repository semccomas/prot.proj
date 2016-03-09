f= open ('./SVM/svm_input/point1_output1.txt', 'r')
fread= f.read().splitlines()


g= open ('./SVM_BLAST/psi_clean_with_feat.txt', 'r')
gread= g.read().splitlines()
'''
for line in fread:
	line= line.split()
	#print line [0]

	#above takes only the target value for point1 outputs


	for array in gread:
		print line [0], ':', array '''


########################################### THIS ONE ABOVE ###############################
	#this will print the two next to each other. Now it is just to make the files in the right order...





#for a , b in zip (fread, gread):
#	print a.split()[0], ':',  b , '\n'
"""
file= open('membrane-alpha.3line', 'r')
fread= file.read().splitlines()

out=open('ac_name_with_myseqFASTA_numb.txt', 'w')

seqcount= 1 

for line in fread:
	if '>' in line:
		membname= line
		seqcount= seqcount+1
		out.write(line + '  ' + str(seqcount) + '\n')

out.close
 
####################THIS ONE ALSO REALLY BIG #######################
#check out the output and you will understand. INCLUDE IN UNTITLED IF YOU USE IT !!!!!!!!!!!!!!!
#maybe you can do a dict with this??


"""


cluster= open('./output/point2_output_1.txt')
cluster= cluster.read().splitlines()

readout= open('ac_name_with_myseqFASTA_numb.txt', 'r')
readout= readout.read().splitlines()

name_dic= {}
for line in readout:
	line= line.split()
	acname=line[0]
	num= line[1]
	name_dic [acname]= num
#print name_dic                   #yes I have checked and although the dict isn't in order, the key and values match the ac_name_with file


for acc in cluster:
	if acc in name_dic:
		print acc , name_dic[acc]
		


		


'''

for (seq, name) in zip(cluster, readout):
	if '>' in seq and seq in name:
	#	name= seq
	#	if name in readout:
	#		print name
			print seq, name 




'''









'''
#if name == membname:
#print membname , name
#if < in line in pt2o1 and is also in the out file then print that line in that order
count = 0

import os
for file in os.listdir("/Users/semccomas/Desktop/prot.proj/FASTA_files"):

#r= open ('/output/point*.txt' ,'r')
#rrread= r.read()

	count = count + 1
	if os.path.exists("/Users/semccomas/Desktop/prot.proj/FASTA_files"): 
		if file.endswith('.txt'):
			newfile= file.split('.')[0]
			if newfile.endswith(str(count)):
				print newfile

    #if file.endswith(".txt"):
     #   print(file)


'''






