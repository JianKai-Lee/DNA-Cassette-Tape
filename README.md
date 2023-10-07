# Usage

## Sequence_analysis

To run sequence analysis, put the following files in one folder:  
`A.py`  (For SNP)  
`T.py`  
`C.py`  
`G.py`  
`Sequence_analysis.sh`  (Main codes in command lines) 

In the same folder, you need to provide your data and rename as the following:  
`Sample_1.fq.gz`  (Raw data #1)  
`Sample_2.fq.gz`  (Raw data #2)  
`pool.fasta`  (The pool for matching)  

In our tests, the program ran on a M1 chip MacBook. Due to the compatibility issues, the following tool was also provided in the folder as Unix executable file:  
`flash2`  

You may need to edit the lines in `Sequence_analysis.sh` to fit your data parameters to initiate an analysis.  

Open the folder in Terminal and run the command:  
`./Sequence_analysis.sh`

2023
