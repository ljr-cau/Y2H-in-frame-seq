import sys
id_list=[]
gene_id=open(sys.argv[1],'r')
reads_counts=open(sys.argv[2],'w')
for line in gene_id:
    line=line.replace('\n','')
    id_list.append(line)
id_dict={}
for id in id_list:
    if (id not in id_dict):
        id_dict[id]=0
    id_dict[id]+=1
for element in id_dict.keys():
    reads_counts.write(str(element)+'\t'+str(id_dict[element])+'\n')
