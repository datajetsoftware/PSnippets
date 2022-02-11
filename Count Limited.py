#selects only those values with a count greater than 1% of total
import sys

#input and output files from first 2 arguments, count file is 3  
inputfile = sys.argv[1]
outputfile = sys.argv[2]
countfile = sys.argv[3]

#read input file into array
iFile = open(inputfile, 'r') 
inputArray = iFile.read().splitlines() 
iFile.close()

#read count file into array
cFile = open(countfile, 'r') 
countArray = cFile.read().splitlines() 
cFile.close()
    
total = float(0)
for count in countArray:
    total += float(count)    
    
n = len(inputArray)

oFile = open(outputfile, 'w') 
for x in range(0,n):
    pc = float(countArray[x]) / total
    if pc > 0.01: #change this percentage
        processed=inputArray[x]
    else:
        processed=''
    oFile.write(processed+'\n')
oFile.close()