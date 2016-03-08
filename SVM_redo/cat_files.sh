INPUT_DIR=/Users/semccomas/Desktop/prot.proj/SVM_redo/svm_input2

for i in $INPUT_DIR/SVM_set_*.txt; do
	for j in $INPUT_DIR/SVM_set_*.txt
	do
		base=`basename $i .txt`
		if [ $j = $INPUT_DIR/SVM_set_1.txt ]; then
			continue
		fi
		if [ $i = $INPUT_DIR/SVM_set_1.txt ]; then
			continue
		fi
		if [ $i != $j ];then
			cat $j >> $INPUT_DIR/$base.train.txt
		fi
	done
done