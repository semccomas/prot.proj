#program for comparing the prediction results to MCC

import sys                          #to use for sys.argv[]
script_name= sys.argv[0]
input_file = sys.argv[1]            # so that you can only write 'python point1new.py input_file_name'
input_file_SVM= sys.argv[2]
output_file= sys.argv[3]
file=open(input_file)                  #need to open the input file
file_SVM= open(input_file_SVM)
fileread=file.read().splitlines()            #splitting to read line by line, will need in i1
file_SVM=file_SVM.read().splitlines()
o= open(output_file, 'w')


count=0
for a, b in zip (fileread, file_SVM):
	target_val= a[0]
	target_SVM= b[0]
	count= count+ 1
	p= '#' + str(count) +'\n'
	if target_val == '-' and target_SVM == '-':
		o.write('TN ' + p)
	elif target_val != '-' and target_SVM !='-':
		o.write('TP ' + p)
	elif target_val != '-' and target_SVM == '-':
		o.write('FN '+ p)
	elif target_val == '-' and target_SVM != '-':
		o.write('FP ' + p)

o.close


#this file seems to work. Double check that the FN and FP are supposed to be if the predictor is wrong 
#the SVM pred file is much longer, like thousands of characters longer. Do we care? 