# Y2H-in-frame-seq User Guide
#### version 1.0

## Table of contents
- [What is Y2H-in-frame-seq?](#What-is-Y2H-in-frame-seq)
- [Usage](#Usage)
  + [Step 1 : Trimming vector sequence](#Step-1--Trimming-vector-sequence)
  + [Step 2 : Mapping trimmed reads to CDS](#Step-2--Mapping-trimmed-reads-to-CDS)
  + [Step 3 : Collecting the in-frame reads](#Step-3--Collecting-the-in-frame-reads)
  + [Step 4 : Translating the in-frame reads into polypeptides](#Step-4--Translating-the-in-frame-reads-into-polypeptides)
  + [Step 5 : Removing short ORF](#Step-5--Removing-short-ORF)
  + [Step 6 : Calculating read-count](#Step-6--Calculating-read-count) 
- [Outputs](#Outputs)
- [Related Efforts](#related-efforts)
- [Maintainers](#maintainers)


## What is Y2H-in-frame-seq?

<img src="https://github.com/ljr-cau/Y2H-in-frame-seq/blob/main/images/logo.png" width=300>

The yeast two-hybrid (Y2H) system is a powerful binary interaction assay that has been widely used for large-scale screening of interacting proteins within well-constructed ORFeomes or raw cDNA libraries. However, Y2H screening with cDNA libraries would result in false positive and/or false negative, which may be caused by a large fraction of non-natural ORFs contained in cDNA libraries. Thus, we developed a novel simple NGS-based method (named Y2H-in-frame-seq) to accomplish a more precise Y2H screening with cDNA libraries. By using newly designed primers, the NGS reads containing 5’ end of prey inserts were dramatically enriched (see Gu et al., 2021 for more details). With 5’ end information, we can distinguish and filter out those non-in-frame reads from all mapped reads, which further improves the estimation of the interaction intensity between bait and prey.

Comparing to canonical NGS-based Y2H method, our new method doesn’t need to generate a new cDNA library or to change the workflow of classic Y2H-NIGS protocol. The only change you should follow is to synthesize a pair of primers and use our Python script (or other compatible software). The experimental design of Y2H-in-frame-seq is also compatible with recently developed quantification methods, such as [NGPINT](https://github.com/Wiselab2/NGPINT)/[Y2H-SCORES](https://github.com/Wiselab2/Y2H-SCORES) (Banerjee et al., 2020; Velasquez-Zapata et al., 2021). 



#### Citation
- Yinghui Gu, Guannan Li, Ping Wang, Yan Guo, Jingrui Li (2021). A simple and precise method (Y2H-in-frame-seq) improves yeast two-hybrid screening with cDNA libraries. Journal of Genetics and Genomics. [(URL)](https://www.sciencedirect.com/science/article/abs/pii/S1673852721003611)

#### Other Softwares 
- [Cutadapt](https://cutadapt.readthedocs.io/en/stable/)
- [Hisat2](http://daehwankimlab.github.io/hisat2/)
- [SAMtools](http://samtools.sourceforge.net/)
- [fq_all2std.pl](https://github.com/josephhughes/Sequence-manipulation/blob/master/fq_all2std.pl)
- [FilterSamReads(Picard)](https://gatk.broadinstitute.org/hc/en-us/articles/360036882611-FilterSamReads-Picard-)


## Usage

Either single-end or paired-end sequencing data can be used and only the Read_1 is needed.

### Step 1 : Trimming vector sequence
```
$ cutadapt -g CCATGGAGGCCAGTGAATTCGGCACGAGG -m 10 -o output.cutadapt.fastq clean.fastq  
```

“CCATGGAGGCCAGTGAATTCGGCACGAGG” is our vector sequence, you should change the sequence according your vector. 

### Step 2 : Mapping trimmed reads to CDS
```
$ hisat2 -p 10 -x /path_to_CDS_index_file/index_file_name -U output.cutadapt.fastq -S output.sam
```

### Step 3 : Collecting the in-frame reads
```
$ python capture_mapped.py output.sam output_mapped.sam
$ python inframe.py output_mapped.sam output_inframe.sam
```

The inframe.py script can distinguish in-frame reads from non-inframe reads by using the position information in SAM file.

### Step 4 : Translating the in-frame reads into polypeptides
```
$ samtools fastq output_inframe.sam > output_inframe.fastq
$ perl fq_all2std.pl fq2fa output_inframe.fastq > output_inframe.fa
$ python translate.py output_inframe.fa > output_inframe.aa
```

### Step 5 : Removing short ORF
```
$ grep -B 1 '*' output_inframe.aa > output_inframe_STOP_list.txt
$ grep '>' output_inframe_STOP_list.txt > output_inframe_STOP_ID.list
$ sed -i 's/.//' output_inframe_STOP_ID.list
$ picard FilterSamReads -I output_inframe.sam -O output_inframe_filtered.sam --READ_LIST_FILE output_inframe_STOP_ID.list --FILTER excludeReadList
```

The in-frame reads that encoding a shorter polypeptide (less than 30 amino acids) are removed at this step. 

### Step 6 : Calculating read-count 
```
$ python find_mapped_gene.py output_inframe_filtered.sam output_inframe_filtered_ID.list
$ python cal_reads_counts.py output_inframe_filtered_ID.list output_inframe_filtered_read_count.txt

$ python find_mapped_gene_2.py output_inframe_filtered.sam output_inframe_filtered_ID_Start_Position.list
$ python rm_duplicate.py output_inframe_filtered_ID_Start_Position.list output_inframe_filtered_ID_Start_Position_rmdup.list
$ awk '{print $1}' output_inframe_filtered_ID_Start_Position_rmdup.list > output_inframe_filtered_ID_rmdup.list
$ python cal_reads_counts.py output_inframe_filtered_ID_rmdup.list output_inframe_filtered_unique_read_count.txt
```


## Outputs
### You can check the results files. ###
- ### output_inframe.aa ###
```
$ head output_inframe.aa
```
<img src="https://github.com/ljr-cau/Y2H-in-frame-seq/blob/main/images/output_inframe.aa.jpg" width=300>

- ### output_inframe_STOP_list.txt ###
```
$ head output_inframe_STOP_list.txt
```
<img src="https://github.com/ljr-cau/Y2H-in-frame-seq/blob/main/images/output_inframe_STOP_list.png" width=300>

- ### output_inframe_STOP_ID.list ###
```
$ head output_inframe_STOP_ID.list
```
<img src="https://github.com/ljr-cau/Y2H-in-frame-seq/blob/main/images/output_inframe_STOP_ID.list.png" width=300>

- ### ooutput_inframe_filtered_read_count.txt ###
```
$ head output_inframe_filtered_read_count.txt
```
<img src="https://github.com/ljr-cau/Y2H-in-frame-seq/blob/main/images/output_inframe_filtered_read_count.png" width=180>
  
#### Columns in this order ####
  - **Transcript-ID**
  - **read-count**
  

## Related Efforts
[NGPINT](https://github.com/Wiselab2/NGPINT)/[Y2H-SCORES](https://github.com/Wiselab2/Y2H-SCORES)

## Maintainers
[@ljr-cau](https://github.com/ljr-cau).
