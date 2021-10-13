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

## What is MutMap?
<img src="https://github.com/YuSugihara/MutMap/blob/master/images/1_logo.png" width=200>

Bulked segregant analysis, as implemented in MutMap ([Abe et al., 2012](https://www.nature.com/articles/nbt.2095)), is a powerful and efficient method to identify agronomically important loci in crop plants. MutMap requires whole-genome resequencing of a single individual from the original cultivar and the pooled sequences of F2 progeny from a cross between the original cultivar and mutant. MutMap uses the sequence of the original cultivar to polarize the site frequencies of neighbouring markers and identifies loci with an unexpected site frequency, simulating the genotype of F2 progeny. **The updated pipeline is approximately 5-8 times faster than the previous pipeline, are easier for novice users to use and can be easily installed through bioconda with all dependencies.**

#### Citation
- Yinghui Gu, Guannan Li, Ping Wang, Yan Guo, Jingrui Li. A simple and precise method (Y2H-in-frame-seq) improves yeast two-hybrid screening with cDNA libraries. Under revision
