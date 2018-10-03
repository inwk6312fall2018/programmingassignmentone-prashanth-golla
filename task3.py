#opening a file
fin=open('running-config.cfg')
#creating empty lists to save the output
global_access=[]
management_access_in=[]
for line in fin:                     # takes each line separately
#removing whitespaces  
  line=line.strip()
  line=line.split()
  if(line[0]=='access-list' and line[1]=='global_access'):
    global_access.append(line)          # if expression satisfies then it appends the line to the empty list
  if(line[0]=='access-list' and line[1]=='fw-management_access_in'):
    management_access_in.append(line)
print(global_access)
print(management_access_in)
