
import sys

#input and output files from first 2 arguments  
inputfile = sys.argv[1]
outputfile = sys.argv[2]
countsfile = sys.argv[3]

#read input file into array
iFile = open(inputfile, 'r') 
inputArray = iFile.read().splitlines() 
iFile.close()

    

oFile = open(outputfile, 'w') #write to file
for line in inputArray:
#
    try:
        #process the lines here
        processed = line #simply copies the source string
    except:
        processed="" #assign to null on exception
#endif    
#
    oFile.write(processed+'\n') 
oFile.close()
                        