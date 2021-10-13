# Y2H-in-frame-seq User Guide
#### version 1.0

## Table of contents
- [What is Y2H-in-frame-seq?](#What-is-Y2H-in-frame-seq)

- [Usage](#Usage)
  + [Step 1 : trim of vector sequence](#trim-of-vector-sequence)
  + [Step 2 : calculate the ORF](#calculate-the-ORF)
  + [Step 3 : translate the ORF into peptides](#translate-the-ORF-into-peptides])
  + [Step 5 : sum the abundance from SAM file](#sum-the-abundance-from-SAM-file)
- [Outputs](#Outputs)

## What is Y2H-in-frame-seq?
<img src="https://github.com/YuSugihara/MutMap/blob/master/images/1_logo.png" width=200>

The yeast two-hybrid (Y2H) system is a powerful binary interaction assay that has been widely used for large-scale screening of interacting proteins within well-constructed ORFeomes or raw cDNA libraries. Recently, the next-generation sequencing (NGS) was adapted to Y2H screening which significantly increased the efficiency and sensitivity, while reducing the labor and experimental cost. We developed a novel simple NGS-based method (named Y2H-in-frame-seq) to accomplish a more precise Y2H screening with cDNA libraries. By using newly designed primers, the NGS reads containing 5’ end of prey inserts were dramatically enriched. With 5’ end information, we can distinguish and filter out those non-in-frame reads from all mapped reads, which further improves the estimation of the interaction intensity between bait and prey. The experimental design of our new method is also compatible with some recently developed quantification methods (Banerjee et al., 2020; Velasquez-Zapata et al., 2021). Thus, a combination of our Y2H-in-frame-seq and NGPINT/Y2H-SCORES was also highly recommanded.



#### Citation
- Yinghui Gu, Guannan Li, Ping Wang, Yan Guo, Jingrui Li. A simple and precise method (Y2H-in-frame-seq) improves yeast two-hybrid screening with cDNA libraries. Under revision
