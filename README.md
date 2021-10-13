# Y2H-in-frame-seq User Guide
#### version 1.0

## Table of contents
- [What is Y2H-in-frame-seq?](#What-is-Y2H-in-frame-seq)

- [Usage](#Usage)
  + [Step 1 : Trimming of the vector sequence](#trimming-of-the-vector-sequence)
  + [Step 2 : Mapping the trimmed reads to CDS file](#mapping-the-trimmed-reads-to-CDS-file)
  + [Step 3 : Collection of the in-frame reads](#collection-of-the-in-frame-reads)
  + [Step 4 : Translate the in-frame reads into polypeptides](#translate-the-in-frame-reads-into-polypeptides])
  + [Step 5 : Removal of short ORF](#removal-of-short-ORF)
  + [Step 6 : Calculate read-count](#calculate-read-count)


- [Outputs](#Outputs)

## What is Y2H-in-frame-seq?

The yeast two-hybrid (Y2H) system is a powerful binary interaction assay that has been widely used for large-scale screening of interacting proteins within well-constructed ORFeomes or raw cDNA libraries. Recently, the next-generation sequencing (NGS) was adapted to Y2H screening which significantly increased the efficiency and sensitivity, while reducing the labor and experimental cost. We developed a novel simple NGS-based method (named Y2H-in-frame-seq) to accomplish a more precise Y2H screening with cDNA libraries. By using newly designed primers, the NGS reads containing 5’ end of prey inserts were dramatically enriched. With 5’ end information, we can distinguish and filter out those non-in-frame reads from all mapped reads, which further improves the estimation of the interaction intensity between bait and prey. The experimental design of our new method is also compatible with some recently developed quantification methods (Banerjee et al., 2020; Velasquez-Zapata et al., 2021). Thus, a combination of our Y2H-in-frame-seq and NGPINT/Y2H-SCORES was also highly recommanded.

#### Citation
- Yinghui Gu, Guannan Li, Ping Wang, Yan Guo, Jingrui Li. A simple and precise method (Y2H-in-frame-seq) improves yeast two-hybrid screening with cDNA libraries. Under revision

#### Other Softwares 
- [cutadapt](https://cutadapt.readthedocs.io/en/stable/)
- [Hisat2](http://daehwankimlab.github.io/hisat2/)
- [SAMtools](http://samtools.sourceforge.net/)
- [fq_all2std.pl](https://github.com/josephhughes/Sequence-manipulation/blob/master/fq_all2std.pl)
- [FilterSamReads(Picard)](https://gatk.broadinstitute.org/hc/en-us/articles/360036882611-FilterSamReads-Picard-)


## Usage

Current version can not automatically make the plots as shown in paper.
**Thus, We highly recommend you to choose other tools, such as Y2H-SCORES.**

### Step 1 : Trimming of the vector sequence
```

$ cutadapt -g CCATGGAGGCCAGTGAATTCGGCACGAGG -m 10 -o output.cutadapt.fastq clean.fastq
       
```

**“CCATGGAGGCCAGTGAATTCGGCACGAGG”** is our vector sequence, you should change the sequence to your vector 


### Step 2 : Mapping the trimmed reads to CDS file
```

$ hisat2 -p 10 -x /path_to_CDS_index_file/index_file_name -U output.cutadapt.fastq -S output.sam

```

### Step 3 : Collection of in-frame reads
```

$ python capture_mapped.py output.sam output_mapped.sam

$ python inframe.py output_mapped.sam output_inframe.sam

```

### Step 4 : Translate the in-frame reads into polypeptides
```

$ samtools fastq output_inframe.sam > output_inframe.fastq

$ perl fq_all2std.pl fq2fa output_inframe.fastq > output_inframe.fa

$ python translate.py output_inframe.fa > output_inframe.aa

```

### Step 5 : Removal of short ORF

```

$ grep -B 1 '*' output_inframe.aa > output_inframe_STOP_list.txt

$ grep '>' output_inframe_STOP_list.txt > output_inframe_STOP_ID.list

$ sed -i 's/.//' output_inframe_STOP_ID.list

$ picard FilterSamReads -I output_inframe.sam -O output_inframe_filtered.sam --READ_LIST_FILE output_inframe_STOP_ID.list --FILTER excludeReadList

```
### Step 6 : Calculate read-count

```
$ python find_mapped_gene.py output_inframe_filtered.sam output_inframe_filtered_ID.list

$ python cal_reads_counts.py output_inframe_filtered_ID.list output_inframe_filtered_read_count.txt

```


