INPUT_DIR=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/SVM/svm_input

for i in $INPUT_DIR/point1_output*.txt; do
	for j in $INPUT_DIR/point1_output*.txt
	do
		if [ $j = $INPUT_DIR/point1_output1.txt ]; then
			continue
		fi
		if [ $i = $INPUT_DIR/point1_output1.txt ]; then
			continue
		fi
		if [ $i != $j ];then
			cat $j >> $i.training.
		fi
	done
done