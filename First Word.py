import sys

#input and output files from first 2 arguments  
inputfile = sys.argv[1]
outputfile = sys.argv[2]

#read input file into array
iFile = open(inputfile, 'r') 
inputArray = iFile.read().splitlines() 
iFile.close()

    

oFile = open(outputfile, 'w') #write to file
for line in inputArray:
    tokens = line.split(' ')
    if len(tokens) > 0:
        processed=tokens[0]
    else:
        processed=''
    oFile.write(processed+'\n')
oFile.close()