
import sys

#input and output files from first 2 arguments  
inputfile = sys.argv[1]
outputfile = sys.argv[2]
countsfile = sys.argv[3]

#set a default value for left, for testing
left=2
#but if param is present then acquire new value for left
if(len(sys.argv)==5):
    left = int(sys.argv[4])

#read input file into array
iFile = open(inputfile, 'r') 
inputArray = iFile.read().splitlines() 
iFile.close()

    

oFile = open(outputfile, 'w') #write to file
for line in inputArray:
#
    try:
        #process the lines here
        processed = line[0:min(left,len(line))] #simply copies the source string
    except:
        processed="error" #assign to null on exception
#endif    
#
    oFile.write(processed+'\n') 
oFile.close()
                        