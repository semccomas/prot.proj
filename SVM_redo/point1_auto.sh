#point1 automated for BLAST
#you will have to change this when you run it in your machine. It is like this now because you are re-doing the old SVMs 
#then send this and all the models and training to the machine
INPUT_DIR=/Users/semccomas/Desktop/prot.proj
OUTPUT_DIR=/Users/semccomas/Desktop/prot.proj
SCRIPT_DIR=/Users/semccomas/Desktop/prot.proj






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


database_file=/home/sarah/Desktop/prot.proj.scilifecomp/BLAST_proj/uniref90.fasta
input_dir=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/FASTA_files
output_dir=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/outputs_BLAST

#use .blastpgp
#or .psi?

for i in $input_dir/*.fasta ; do
base=`basename $i .fasta`
if [ ! -f $output_dir/$base.psi ] ; then
	blastpgp -i $i -j 3 -d $database_file -i $i -o $output_dir/$base.blastpgp -Q $output_dir/$base.psi
fi
done
echo "I'm done!!!! Yeah!"