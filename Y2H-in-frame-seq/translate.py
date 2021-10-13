import sys
fa_file=open(sys.argv[1],'r')
protein_file=open(sys.argv[2],'w')
for line in fa_file:
    if ">" in line:
        protein_file.write(line)
    if ">" not in line:
        if len(line) < 90:
            protein_file.write("*"+'\n')
        if len(line) >= 90:

            codon_table = {
                'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A', 'CGT':'R', 'CGC':'R',
                'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R', 'TCT':'S', 'TCC':'S',
                'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S', 'ATT':'I', 'ATC':'I',
                'ATA':'I', 'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L',
                'CTG':'L', 'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G', 'GTT':'V',
                'GTC':'V', 'GTA':'V', 'GTG':'V', 'ACT':'T', 'ACC':'T', 'ACA':'T',
                'ACG':'T', 'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 'AAT':'N',
                'AAC':'N', 'GAT':'D', 'GAC':'D', 'TGT':'C', 'TGC':'C', 'CAA':'Q',
                'CAG':'Q', 'GAA':'E', 'GAG':'E', 'CAT':'H', 'CAC':'H', 'AAA':'K',
                'AAG':'K', 'TTT':'F', 'TTC':'F', 'TAT':'Y', 'TAC':'Y', 'ATG':'M',
                'TGG':'W', 'TAG':'*', 'TGA':'*', 'TAA':'*', 'TT\n':'*'}
            prot=''
            for i in range(0,90,3):
                if "N" in line[i:i+3]:
                    prot+="*"
                if "N" not in line[i:i+3]:
                    prot+=codon_table[line[i:i+3]]
            protein_file.write(prot+'\n')
        #elif len(line) < 90:
         #   protein_file.write("*")
