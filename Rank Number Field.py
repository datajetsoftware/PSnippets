
import sys

#input and output files from first 2 arguments  
inputfile = sys.argv[1]
outputfile = sys.argv[2]
countsfile = sys.argv[3]

#read input file into array
iFile = open(inputfile, 'r') 
inputArray = iFile.read().splitlines() 
iFile.close()


li=[]
  
for i in range(len(inputArray)):
      li.append([float(inputArray[i]),i])
li.sort()
sort_index = []
  
for x in li:
      sort_index.append(x[1])
  

   

oFile = open(outputfile, 'w') #write to file

for line in sort_index:
#
    try:
        #process the lines here
        processed = str(line) #simply copies the source string
    except:
        processed="" #assign to null on exception
#endif    
#
    oFile.write(processed+'\n') 
oFile.close()
                        