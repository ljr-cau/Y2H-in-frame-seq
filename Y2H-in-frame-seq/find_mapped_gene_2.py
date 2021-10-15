import sys
import re
sam_data=open(sys.argv[1],'r')
inframe_data=open(sys.argv[2],'w')
for line in sam_data:
    if "@" not in line:
        element=line.split('\t')
        if element[2] != "*":
            inframe_data.write(element[2]+'\t'+element[3]+'\n')
sam_data.close()
