#script_file=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/SVM_BLAST/testingBLAST
#input_dir=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/SVM_BLAST/testingBLAST
#output_dir=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/SVM_BLAST/testingBLAST


script_file=/Users/semccomas/Desktop/prot.proj/SVM_BLAST/testingBLAST
input_dir_OG_set=/Users/semccomas/Desktop/prot.proj/SVM/svm_input
input_dir_SVM=/Users/semccomas/Desktop/prot.proj/SVM/models_terminal_outputs_svm
output_dir_TP_TN=/Users/semccomas/Desktop/prot.proj/SVM
output_dir_MCC_num=/Users/semccomas/Desktop/prot.proj/SVM

count=2
for i in $input_dir_OG_set/point1_output$count.txt ; do           #here this will be BLAST_SVM_set2.txt
base=`basename $i `                                                 #base= point1_output2 here.
for j in $input_dir_SVM/prediction_results3456.txt; do
if [ -f $j ] ; then              #here this will be predicted_results2.txt. So itll be input_dir_SVM predicted_results$count.txt because you have to be specific. That is why here i just choose one file.
	echo $base
	python $script_file/svm_pred_MCC.py $i $j $output_dir_TP_TN/prediction_assessment3456.txt $output_dir_MCC_num/mcc_num_set$count.txt        #the last one will be the same as you have in the machine. TP_TN output will be called TNTP comparison
	let count=count+1
fi
done
done
echo $count