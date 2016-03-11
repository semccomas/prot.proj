#this will cat the 5 sets together. sort based on prediction tv's and then be ready to input to the ROC curve

import operator as op


filenames_SVM = ['./SVM/models_terminal_outputs_svm/prediction_results2345.txt', './SVM/models_terminal_outputs_svm/prediction_results2346.txt', './SVM/models_terminal_outputs_svm/prediction_results2356.txt', './SVM/models_terminal_outputs_svm/prediction_results2456.txt', './SVM/models_terminal_outputs_svm/prediction_results3456.txt']
with open('./SVM/models_terminal_outputs_svm/ALL_predicted_results.txt', 'w') as outfile_SVM:
    for fname in filenames_SVM:
        with open(fname) as infile:
            for line in infile:
                outfile_SVM.write(line)
outfile_SVM.close


filenames_actual = ['./SVM/svm_input/point1_output6.txt', './SVM/svm_input/point1_output5.txt', './SVM/svm_input/point1_output4.txt', './SVM/svm_input/point1_output3.txt', './SVM/svm_input/point1_output2.txt']
with open('./SVM/models_terminal_outputs_svm/ALL_actual_results.txt', 'w') as outfile_actual:
    for fname2 in filenames_actual:
        with open(fname2) as infile2:
            for line2 in infile2:
            	line2=str(line2).split()
            	#line2=[line2]
                outfile_actual.write(line2[0]+'\n')
outfile_actual.close


sortedfile=open('./SVM/models_terminal_outputs_svm/ALL_actual_results.txt', 'r')
sorted_SVM=open('./SVM/models_terminal_outputs_svm/ALL_predicted_results.txt', 'r')

newfile=open('./SVM/models_terminal_outputs_svm/SORTED.txt', 'w')


for (a,b) in zip(sorted_SVM, sortedfile):
	#a=(a).strip('\n') 
	#b=(b).strip('\n') 
									# newfile.write (a + '  ' + b ) = NO. Does not put them on the same line
	r= [(a + ' , ' +  b)]                 #r is a LIST 
	#newfile.write( r[0] )
	r= r[0]
	r= r.split(',')
	newfile.write( r[0]  )                        #!!!! I don't really know why but this way makes r[0] accessible, if i dont have r[0] and r.split it is not

newfile.close

	#print op.itemgetter(0)(r)
	#getcount=op.itemgetter(0)
	#print sorted(r, key=getcount)




#for (aa, bb, cc, dd, ee) in zip (a, v, b, c, d, e):
#	l.append(aa, bb, cc, dd, ee)
#	print l
#	f.write(aa + 'HELLO HELLO HELLO' + vv + 'VVVVV' +  " " + bb + " " + cc + " " + dd + " " + ee + " ")

#f.close
'''
lister2=[]
for (aa, vv, bb, ww, cc, xx, dd, yy, ee, zz) in zip(a, v, b, w, c, x, d, y, e, z):
	vv= str(vv).split()
	ww= str(ww).split()
	xx= str(xx).split()
	yy= str(yy).split()
	zz= str(zz).split()
	lister2.append(aa + '  ' + vv[0] + '\n' + bb + '  ' + ww[0] + '\n' + cc + '  ' + xx[0] + '\n' + dd + '  ' + yy[0] + '\n' + ee + '  ' + zz[0] + '\n')
	h.write(aa + '  ' + vv[0] + '\n' + bb + '  ' + ww[0] + '\n' + cc + '  ' + xx[0] + '\n' + dd + '  ' + yy[0] + '\n' + ee + '  ' + zz[0] + '\n')

h.close

print lister2

#i= open('./SVM/models_terminal_outputs_svm/actual_cat_for_ROC.txt', 'r')
#j= open('./SVM/models_terminal_outputs_svm/predictions_cat_for_ROC.txt', 'r')

k= open('./SVM/models_terminal_outputs_svm/sorted_cats_for_ROC.txt', 'r')


from operator import itemgetter

getvalue=itemgetter(0)
#def getKey(item):
	#return item[0]
lister= []
for (ii) in k:
	ii= str(ii).split()
	lister.append(ii)
#print lister
	#xxx= sorted(k, key= getvalue)
	#print xxx

	#for line in xxx:
		#print line 

		'''

