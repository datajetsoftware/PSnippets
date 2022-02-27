
import sys

N=3    #want the top N by count; the rest into other. null stays null

#input and output files from first 2 arguments  
inputfile = sys.argv[1]
outputfile = sys.argv[2]
countsfile = sys.argv[3]

#read input file into array
iFile = open(inputfile, 'r') 
inputArray = iFile.read().splitlines() 
iFile.close()

cFile = open(countsfile, 'r') 
tempArray = cFile.read().splitlines() 
cFile.close()

size = len(inputArray)

counts=[]
for x in range(0,size):
    counts.append(int(tempArray[x]))

            
sorted_counts = sorted(counts)
sorted_counts.reverse()
            
threshold = sorted_counts[min(N-1,len(counts)-1)]           
        

oFile = open(outputfile, 'w') #write to file
for x in range(0,size):
#
    try:
        #process the lines here
        
        if counts[x] >= threshold:
            processed = inputArray[x] #simply copies the source string
        else:
            processed = "Other"
    except:
        processed="error" #assign to null on exception
#endif    
#
    oFile.write(processed+'\n') 
oFile.close()
                        