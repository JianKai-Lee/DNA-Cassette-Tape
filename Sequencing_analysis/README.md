# Usage

## **Dependencies**
Before running this pipeline, ensure the following tools are installed and accessible in your `PATH`:
- **FLASH2**: Merge paired-end reads.  
- **cutadapt**: Trim primers.  
- **bwa & samtools**: Alignment and BAM processing.  
- **seqtk**: Quality filtering.  

In our tests, the program ran on a M1 chip MacBook. Due to the compatibility issues, the following tool was also provided in the folder as Unix executable file:  
- **FLASH2**

## Sequencing_analysis
**Inputs**: 

To run sequencing analysis, put the following files in one folder:  
`Sequencing_analysis.sh`  (Main codes in command lines) 

In the same folder, you need to provide your data and rename as the following:  
`Sample_1.fq.gz`  (Sequencing raw data #1)  
`Sample_2.fq.gz`  (Sequencing raw data #2)  
`pool.fasta`  (The pool for matching)  



You may need to edit the lines in `Sequence_analysis.sh` to fit your data parameters to initiate an analysis.  

**Run**: 

Open the folder in Terminal and run the following commands. 

Nevigate to your path: `cd PATH/TO/YOUR/FOLDER`

Give premission: `chmod +x Sequencing_analysis.sh`

Run the code: `./Sequencing_analysis.sh`

