import sys
import re
sam_data=open(sys.argv[1],'r')
inframe_data=open(sys.argv[2],'w')
for line in sam_data:
    if "@" in line:
        #print line
        inframe_data.write(line) 
    if "@" not in line:
        element=line.split('\t')
        if element[2] != "*":
            as_value=element[11].split(':')
            if int(as_value[2]) == 0:
                if int(element[3])%3 == 1:
                    #print line
                    inframe_data.write(line)
            if int(as_value[2]) != 0:
                if re.search(r'(.*)S(.*)M',element[5]):
                    mis_match=element[5].split('S')
                    if (int(element[3])%3 == 1 and int(mis_match[0])%3 == 0):
                        inframe_data.write(line)
                    elif (int(element[3])%3 == 2 and int(mis_match[0])%3 == 1):
                        inframe_data.write(line)
                    elif (int(element[3])%3 == 0 and int(mis_match[0])%3 == 2):
                        inframe_data.write(line)
                    
                    #new_position=int(element[3])-int(mis_match[0])
                    #if new_position%3 == 1:
                           #print line
                           #inframe_data.write(line)
sam_data.close()
