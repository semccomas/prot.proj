from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import random
import numpy as np 

#file= open('./SVM_BLAST/testingBLAST/ROC_curve_kernel0_SORTED.txt', 'r').read().splitlines()
file= open('./SVM/models_terminal_outputs_svm/ROC_single_seq_default_SORTED.txt', 'r').read().splitlines()


ilist= [ ]

for i in file:
	i= i.split('	')
	ilist.append(i)


myarray= np.asarray(ilist)
myarray= myarray.astype(np.float)
	
actual= myarray [ : , 0]
predictions= myarray [ : , 1 ]
print actual
print predictions
#print myarray


false_positive_rate, true_positive_rate, thresholds = roc_curve(actual, predictions)
roc_auc = auc(false_positive_rate, true_positive_rate)

#print true_positive_rate

plt.title('Receiver Operating Characteristic')
plt.plot(false_positive_rate, true_positive_rate, 'b',
label='AUC = %0.2f'% roc_auc)
plt.legend(loc='lower right')
plt.plot([0,1],[0,1],'r--')
plt.xlim([-0.1,1.2])
plt.ylim([-0.1,1.2])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()
