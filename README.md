# Y2H-in-frame-seq User Guide
#### version 1.0

## Table of contents
- [What is Y2H-in-frame-seq?](#What-is-Y2H-in-frame-seq)

- [Usage](#Usage)
  + [Step 1 : trim of vector sequence](#trim-of-vector-sequence)
  + [Step 2 : mapping the trimmed reads to CDS file](#calculate-the-ORF)
  + [Step 2 : calculate the ORF](#calculate-the-ORF)
  + [Step 3 : translate the ORF into peptides](#translate-the-ORF-into-peptides])
  + [Step 5 : sum the abundance from SAM file](#sum-the-abundance-from-SAM-file)
- [Outputs](#Outputs)

## What is Y2H-in-frame-seq?

The yeast two-hybrid (Y2H) system is a powerful binary interaction assay that has been widely used for large-scale screening of interacting proteins within well-constructed ORFeomes or raw cDNA libraries. Recently, the next-generation sequencing (NGS) was adapted to Y2H screening which significantly increased the efficiency and sensitivity, while reducing the labor and experimental cost. We developed a novel simple NGS-based method (named Y2H-in-frame-seq) to accomplish a more precise Y2H screening with cDNA libraries. By using newly designed primers, the NGS reads containing 5’ end of prey inserts were dramatically enriched. With 5’ end information, we can distinguish and filter out those non-in-frame reads from all mapped reads, which further improves the estimation of the interaction intensity between bait and prey. The experimental design of our new method is also compatible with some recently developed quantification methods (Banerjee et al., 2020; Velasquez-Zapata et al., 2021). Thus, a combination of our Y2H-in-frame-seq and NGPINT/Y2H-SCORES was also highly recommanded.

#### Citation
- Yinghui Gu, Guannan Li, Ping Wang, Yan Guo, Jingrui Li. A simple and precise method (Y2H-in-frame-seq) improves yeast two-hybrid screening with cDNA libraries. Under revision

#### Other Softwares 
- [cutadapt](https://cutadapt.readthedocs.io/en/stable/)
- [Hisat2](http://daehwankimlab.github.io/hisat2/)
- [SAMtools](http://samtools.sourceforge.net/)
- [BCFtools](http://samtools.github.io/bcftools/)
- [SnpEff](http://snpeff.sourceforge.net/)
- [Trimmomatic](http://www.usadellab.org/cms/?page=trimmomatic)

## Usage

Current version can not automatically make the plots as shown in paper.
**Thus, We highly recommend you to choose other tools, such as Y2H-SCORES.**

### step 1 : trim of vector sequence
```
$ cutadapt -g CCATGGAGGCCAGTGAATTCGGCACGAGG -m 10 -o output.cutadapt.fastq clean.fastq
       
```

**CCATGGAGGCCAGTGAATTCGGCACGAGG** is our vector sequence, you should change the sequence to your vector 


### Step 2 : run MutMap from FASTQ with trimming
```
$ mutmap -r reference.fasta \
         -c cultivar.1.fastq,cultivar.2.fastq \
         -b bulk.1.fastq,bulk.2.fastq \
         -n 20 \
         -o example_dir \
         -T
```

`-r` : reference fasta

`-c` : FASTQs of cultivar. Please input pair-end reads separated by comma. FASTQs can be gzipped.

`-b` : FASTQs of bulk. Please input pair-end reads separated by comma. FASTQs can be gzipped.

`-n` : number of individuals in mutant bulk.

`-o` : name of output directory. Specified name cannot exist.

`-T` : trim your reads by trimmomatic.

### Example 3 : run MutMap from BAM
```
$ mutmap -r reference.fasta \
         -c cultivar.bam \
         -b bulk.bam \
         -n 20 \
         -o example_dir
```

`-r` : reference fasta

`-c` : BAM of cultivar.

`-b` : BAM of bulk.

`-n` : number of individuals in mutant bulk.

`-o` : name of output directory. Specified name cannot exist.

### Example 4 : run MutMap from multiple FASTQs and BAMs
```
$ mutmap -r reference.fasta \
         -c cultivar_1.1.fastq,cultivar_1.2.fastq \
         -c cultivar_1.bam \
         -b bulk_1.1.fastq,bulk_1.2.fastq \
         -b bulk_2.bam \
         -b bulk_3.bam \
         -n 20 \
         -o example_dir