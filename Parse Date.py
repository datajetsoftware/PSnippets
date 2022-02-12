#parse full date
#parse a date string of form  1 April 2020 etc into 2020-04-01
#exceptions will be assigned to null

#then use engineering function String- DATEFROMSTRING(A,B)
#with B = #YYYY-MM-DD to transform this new an actual date field

import sys
from datetime import datetime

#input and output files from first 2 arguments  
inputfile = sys.argv[1]
outputfile = sys.argv[2]

#read input file into array
iFile = open(inputfile, 'r') 
inputArray = iFile.read().splitlines() 
iFile.close()

        

oFile = open(outputfile, 'w') #write to file
for line in inputArray:
    try:
        #adjust format for other incoming formats
        dt = datetime.strptime(line, '%d %B %Y').date()
        processed = str(dt)
    except:
        try:
            dt = datetime.strptime(line, '%d %b %Y').date()
            processed = str(dt)
        except:
            processed=""
    oFile.write(processed+'\n')
oFile.close()
