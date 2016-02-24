#point 1 in project--- date: 2016-02-24
import numpy as np
f=open('../Desktop/myfile.txt', 'r')
aa=f.read().splitlines()

name= aa[0]
seq= list (aa[1])
memb=list (aa[2])

amino= {'A':1, 'C':2, 'E':4, 'D':3, 'G':6, 'F':5, 'I':8, 'H':7, 'K':9, 'M':11,\
'L':10, 'N':12, 'Q':14, 'P':13, 'S':16, 'R':15, 'T':17, 'W':20, 'V':19, 'Y':18}


for q in seq:
    r=[amino[q]]
    print r
for f in memb:
    if f== 'M':
        print 1
    else:
        print 0
        #r.append(f)
        
