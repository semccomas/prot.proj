script_file=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/SVM/svm_light/
input_dir=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/SVM_BLAST/testingBLAST
output_dir=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/SVM_BLAST/testingBLAST

count=1
for i in $input_dir/BLAST_SVM_set*.TRAIN.txt ; do
base=`basename $i `
let count=count+1
if [ ! -f $output_dir/model$count.txt ] ; then
	#echo $base
	$script_file./svm_learn $i $output_dir/model_$base
	echo $count
fi
done
#echo $count