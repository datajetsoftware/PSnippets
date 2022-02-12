
import sys
import math

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


lowr = [-1.5,-1.3125,-1.125,-0.9375,-0.75,-0.5625,-0.375,-0.1875,0,0.1875,0.375,0.5625,0.75,0.9375,1.125,1.3125]
hir = [-1.3125,-1.125,-0.9375,-0.75,-0.5625,-0.375,-0.1875,0,0.1875,0.375,0.5625,0.75,0.9375,1.125,1.3125,1.5]


label = []

for y in range(0,16):
    label.append( str(y).rjust(2, '0') +" "+  str( round(lowr[y]*stdev+avg,2) )+' - ' + str( round(hir[y]*stdev+avg,2) ))


oFile = open(outputfile, 'w') #write to file
for x in range(0,n):

    
    val = float(inputArray[x]) 
    val -= avg
    val /= stdev
    
    processed=""
    for y in range(0,16):
        if(val >= lowr[y] and val < hir[y]):
            processed=label[y] #str(y)
            break;
    



    oFile.write(processed+'\n') 
oFile.close()
                        