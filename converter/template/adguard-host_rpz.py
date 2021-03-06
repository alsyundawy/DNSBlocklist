import os
from re import sub
from shutil import copyfile

infile = some.txt
outfile = some.rpz

f = open(infile,'r')
a = ['||','^']
lst = []
for line in f:
    for word in a:
        if word in line:
            line = line.replace(word,'')
    lst.append(line)
f.close()
f = open(infile,'w')
for line in lst:
    f.write(line)
f.close()

with open(infile) as f:
    file = f.read().split('\n')
for i in range(len(file)):
    file[i] = sub(r'!', ';', file[i])
#print(file)
with open(infile, 'w') as f1:
    f1.writelines(["%s\n" % item  for item in file])
f.close()	

# thanks StackOverFlow
with open(infile, 'r') as f: # load file 
 lines = f.read().splitlines() # read lines
with open(infile, 'w') as f: # load file in write mode
 for line in lines:
  if not line.startswith(';'):
   f.write('\n'.join([line + '  CNAME .\n'])) # add CNAME . if file does not start with ;
f.close()
copyfile(infile, outfile)
os.remove(infile)
# end
