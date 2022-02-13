
import sys
import math

stdRange = 2.5 #lower and upper standard deviations from mean
stdBands = 16 #number of bands
rounding = 0 #rounding for bandings 0=integer


if stdBands==0:
    sys.stderr.write( "stdBands was zero\n" )
    exit()

#input and output files from first 2 arguments  
inputfile = sys.argv[1]
outputfile = sys.argv[2]
countsfile = sys.argv[3]

#read input file into array
iFile = open(inputfile, 'r') 
inputArray = iFile.read().splitlines() 
iFile.close()

#read count file into array
iFile = open(countsfile, 'r') 
scountArray = iFile.read().splitlines() 
iFile.close()
    
n = len(inputArray)


stdIncrement = (stdRange*2)/stdBands

splitAt = []

val = -stdRange

splitAt.append(val)

for x in range(0,stdBands):
    val += stdIncrement
    splitAt.append(val)    



sum = 0.0;
sum2 = 0.0;
tcount = 0.0;

for x in range(0,n):
    count = float(scountArray[x])
    val = float(inputArray[x]) 
    tcount += count;
    sum += count*val
    sum2 += (val*val)*count    
    
if tcount==0:
    sys.stderr.write( "count was zero\n" )
    exit()
    
avg = sum/tcount    
stdev = math.sqrt(sum2/tcount - (avg*avg))

if stdev==0:
    sys.stderr.write( "stdev was zero\n" )
    exit()



for x in range(0,stdBands+1):
    splitAt[x] = round(splitAt[x]*stdev+avg,rounding)
        
lowr = []
hir = []

for x in range(0,stdBands):
    lowr.append(splitAt[x])
    hir.append(splitAt[x+1])




label = []

for y in range(0,stdBands):
    if rounding==0:
        label.append( str(y).rjust(2, '0') +" "+  str( int(lowr[y]) )+' - ' + str( int(hir[y]) ))
    else:        
        label.append( str(y).rjust(2, '0') +" "+  str( lowr[y] )+' - ' + str( hir[y] ))

oFile = open(outputfile, 'w') #write to file
for x in range(0,n):

    
    val = float(inputArray[x]) 
    
    processed=""
    for y in range(0,stdBands):
        if(val >= lowr[y] and val < hir[y]):
            processed=label[y] #str(y)
            break;
    



    oFile.write(processed+'\n') 
oFile.close()
                        