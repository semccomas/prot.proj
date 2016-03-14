: '

BLAST_to_SVM_sets.py		psi_parse_with_topology.py
ROC_curve.py			seq_for_BLAST.py
ROC_curve_prep.py		small_tries.py
point1final.py			structures_for_BLAST.py
point2new.py			untitled.py
psi_matrix_parse.py
psi_parse_automated.sh (the bash_pract is the same ) 


takes a sequence and the model and just returns prediction results
#QUESTIONS: are we just inputting one sequence? How are you going to train on that? 
maybe running blast and see what is related? I wouldnt do much more until you know

assuming you just did have one seq. Enter at pt1. Get the target vals. If you do have mulitple seqs that is
what pt2 is for (making training sets...) if you do have those, start with point 2 (which is just to create cross validated sets) and then do point 1. Thats how 
you did it before. Then if you do blast, do seq_for_BLAST and then run BLAST and then with that output
you will need to do the psi parse automated. From psi parse automated you can run svm. final output would be 
like 3 files. Accuracy, your model, and the MCC calcuation.



!!! Ok so just run PSI-BLAST, then parse output, then classify against your best model from optimization
then you can do mcc and so on.


'


script_dir=/Users/semccomas/Desktop/prot.proj     #here we are using psi_parse_with_topology , 
input_dir=/Users/semccomas/Desktop/prot.proj   #here we will make wherever you're getting your sequence from
blast_dir= /Users/semccomas/Desktop/prot.proj/webserver #here will be the output for where you want your blast files to go. 
output_dir=/Users/semccomas/Desktop/prot.proj/webserver

#for i in $input_dir; do
#	base= `basename $i`
#	blastpgp -i $i -j 3 -d $database_file -i $i -o $blast_dir/$base.blastpgp -Q $blast_dir/$base.psi
#done
#step 1- run blast on file. This is just using the default settings from sarahblast.sh so i think it'll be the same


for f in $input_dir/myseq_FASTA_15_TESTforserver.txt; do     #this will become blast_dir/$base.psi. for now we pretend this 15 file is our blast output (is just a copy from the psi file)
python $script_dir/psi_parse_with_topology_forserver.py $f $output_dir/matrix_SERVERTEST.txt
	done 
#so this step parses the psiblast output. The psiparse file is the same exact file as the original psi_parse but does NOT include stuctures and target values.



