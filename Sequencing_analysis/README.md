# Usage

## Sequencing_analysis

To run sequencing analysis, put the following files in one folder:  
`Sequencing_analysis.sh`  (Main codes in command lines) 

In the same folder, you need to provide your data and rename as the following:  
`Sample_1.fq.gz`  (Sequencing raw data #1)  
`Sample_2.fq.gz`  (Sequencing raw data #2)  
`pool.fasta`  (The pool for matching)  

In our tests, the program ran on a M1 chip MacBook. Due to the compatibility issues, the following tool was also provided in the folder as Unix executable file:  
`flash2`  

You may need to edit the lines in `Sequence_analysis.sh` to fit your data parameters to initiate an analysis.  

Open the folder in Terminal and run the command:  
`./Sequencing_analysis.sh`
