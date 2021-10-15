import sys
list_txt=open(sys.argv[1],'r')
rmdup_list_txt=open(sys.argv[2],'w')
unique=set(list_txt)
for line in unique:
    rmdup_list_txt.write(line)
