echo "Program starts"

#Prepare sequences without primers from raw data. All parameters you may need to adjust are in this block.
./flash2 Sample_1.fq.gz Sample_2.fq.gz -p 33 -r 100 -f 140 -s 100 -o Sample.fq #If you do not have compatibility issues for flash2 and do not have an executable file in the folder, use "/flash2" instead of "./flash2" 
cutadapt -a 'TCCCACCTACCTACAGAGCT' --discard-untrimmed -m 21 -o Sample.fq.extendedFrags_trimend.fastq Sample.fq.extendedFrags.fastq
cutadapt -g 'TTCGGTGTTCAGGTCCTGGC' --discard-untrimmed -m 21 -o Sample.fq.extendedFrags_trimend.fast_aptamer.fastq Sample.fq.extendedFrags_trimend.fastq

#Match the q30 sequences with the given pool
bwa index pool.fasta
echo "Start matching..."
bwa mem pool.fasta Sample.fq.extendedFrags_trimend.fast_aptamer.fastq | samtools view -bSh -q 30 -@ 10 -o Sample_q30_addprimers.bam -
echo "Start sorting..."
samtools sort Sample_q30_addprimers.bam -@ 8 -o Sample_q30.sorted_addprimers.bam
samtools index Sample_q30.sorted_addprimers.bam
samtools view Sample_q30.sorted_addprimers.bam >Sample_q30.sorted_addprimers.sam
awk '{if (/\^/) {print $0}}' Sample_q30.sorted_addprimers.sam>Sample_delet.txt
awk '{if (/SA:Z/) {print $0}}' Sample_q30.sorted_addprimers.sam >Sample_insert.txt
awk '{if(/NM:i:0/) {} else {print $0}}' Sample_q30.sorted_addprimers.sam | awk '{if (/SA:Z/) {} else {print $0}}' | awk '{if (/\^/) {} else {print $0}}'>Sample_snp.txt
awk '{if (/NM:i:0/) {print $0}}' Sample_q30.sorted_addprimers.sam >Sample_perfect_match.txt

#Generate statistics
awk '{print $1"\t"$3"\t"$10}' Sample_perfect_match.txt > Sample_perfect_match_chuli.txt
awk '{print $2}' Sample_perfect_match_chuli.txt | uniq -c >Sample_perfect_match_statistics.txt

#Prepare file for decoding
echo "Start counting reads..."
wc -l Sample.fq.extendedFrags_trimend.fast_aptamer.fastq | awk '{print $1/4}' > total_reads_count.txt
echo "start preparing decoding file. This will take a while..."
seqtk trimfq -q 0.05 -l 21 Sample.fq.extendedFrags_trimend.fast_aptamer.fastq > Sample.trimmed.fastq
awk 'NR%4==2' Sample.trimmed.fastq | sort | uniq -c | sort -nr > Sample_sequence_counts.txt
awk '{print $2}' Sample_sequence_counts.txt > Sample_sequence_sorted.txt

#SNP analysis
echo "SNP starts..."
awk '{if ($12 == "NM:i:1") {print $0}}' Sample_snp.txt | awk '{if (/MD:Z:60/) {} else {print $0}}' > Sample_snp_1.txt
awk '{if ($13~/A/) {print $10"\t"$13}}' Sample_snp_1.txt > Sample_snp_1_A.txt
awk '{if ($13~/T/) {print $10"\t"$13}}' Sample_snp_1.txt > Sample_snp_1_T.txt
awk '{if ($13~/C/) {print $10"\t"$13}}' Sample_snp_1.txt > Sample_snp_1_C.txt
awk '{if ($13~/G/) {print $10"\t"$13}}' Sample_snp_1.txt > Sample_snp_1_G.txt
python3 A.py Sample_snp_1_A.txt | sort | uniq -c >Sample_snp_1_A_num.txt
python3 T.py Sample_snp_1_T.txt | sort | uniq -c >Sample_snp_1_T_num.txt
python3 C.py Sample_snp_1_C.txt | sort | uniq -c >Sample_snp_1_C_num.txt
python3 G.py Sample_snp_1_G.txt | sort | uniq -c >Sample_snp_1_G_num.txt

echo "Program ends"
