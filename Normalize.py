
import sys
import math

#input and output files from first 2 arguments  
inputfile = sys.argv[1]
outputfile = sys.argv[2]


#read input file into array
iFile = open(inputfile, 'r') 
inputArray = iFile.read().splitlines() 
iFile.close()

    
n = len(inputArray)

minv = float(inputArray[0])
maxv = minv

for x in range(1,n):
    val = float(inputArray[x])
    minv = min(minv,val)
    maxv = max(maxv,val)
    
vrange = maxv-minv

oFile = open(outputfile, 'w') #write to file

for x in range(0,n):
    v = float(inputArray[x])
    v = (v-minv)/vrange
    processed = str(round(v,2))
    oFile.write(processed+'\n') 
oFile.close()
                        