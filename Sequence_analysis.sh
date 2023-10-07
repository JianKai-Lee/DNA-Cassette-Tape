echo "Program starts"
echo "This is version 2_1 with auto delete and does not provide SNP analysis"
./flash2 Sample_1.fq.gz Sample_2.fq.gz -p 33 -r 100 -f 140 -s 100 -o Sample.fq
rm Sample_1.fq.gz Sample_2.fq.gz
echo "Flash complete, unzipped files deleted!"
cutadapt -a 'TCCCACCTACCTACAGAGCT' --discard-untrimmed -m 21 -o Sample.fq.extendedFrags_trimend.fastq Sample.fq.extendedFrags.fastq
rm Sample.fq.extendedFrags.fastq
echo "Untrimmed deleted 01"
cutadapt -g 'TTCGGTGTTCAGGTCCTGGC' --discard-untrimmed -m 21 -o Sample.fq.extendedFrags_trimend.fast_aptamer.fastq Sample.fq.extendedFrags_trimend.fastq
rm Sample.fq.extendedFrags_trimend.fastq
echo "Untrimmed deleted 02"
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
rm Sample_q30.sorted_addprimers.sam
rm Sample_q30.sorted_addprimers.bam
rm Sample_q30_addprimers.bam
awk '{print $1"\t"$3"\t"$10}' Sample_perfect_match.txt > Sample_perfect_match_chuli.txt
awk '{print $2}' Sample_perfect_match_chuli.txt | uniq -c >Sample_perfect_match_statistics.txt
echo "statistic complete!"
echo "start counting reads..."
wc -l Sample.fq.extendedFrags_trimend.fast_aptamer.fastq | awk '{print $1/4}' > total_reads_count.txt
echo "start preparing decoding file. This will take a while..."
seqtk trimfq -q 0.05 -l 21 Sample.fq.extendedFrags_trimend.fast_aptamer.fastq > Sample.trimmed.fastq
awk 'NR%4==2' Sample.trimmed.fastq | sort | uniq -c | sort -nr > Sample_sequence_counts.txt
awk '{print $2}' Sample_sequence_counts.txt > Sample_sequence_sorted.txt
rm Sample.trimmed.fastq
echo "Program ends"