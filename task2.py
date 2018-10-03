fin=open('running-config.cfg')
#creating a file result.txt and assiging to write mode
fin1=open('result.txt','w+')
for line in fin:
  line=line.strip()
  line=line.split()
#checks if the first element is security-level
  if(line[0]=='security-level'):
    line[1]='10'
    fin1.write(str(line[1]))
    if(len(line)>=4):
      if(line[2][0:3]=='192' or line[2][0:3]=='172'):
        a=line[2][4:]
        del line[2]
        b='10.'+a
        line.insert(2,b)
      fin1.write(str(line))
    fin1.write(str(line))
