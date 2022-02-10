
import sys
from datetime import datetime

#input and output files from first 2 arguments  
inputfile = sys.argv[1]
outputfile = sys.argv[2]

#read input file into array
iFile = open(inputfile, 'r') 
inputArray = iFile.read().splitlines() 
iFile.close()

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']    

oFile = open(outputfile, 'w') #write to file
for line in inputArray:
    dt = datetime.strptime(line, '%Y-%m-%d').date()
    processed = days[datetime.weekday(dt)]
    oFile.write(processed+'\n')
oFile.close()
