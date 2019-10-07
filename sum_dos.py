import numpy as np
import pandas as pd
import os

##--------------------------------------------------------------------
##   code writen on 20 sept 2019, by Qing W
##            qing.wang@outlook.fr
##This only works for spin-polarized DOS calc. (LORBIT = 11, ICHARGE= 11)
##--------------------------------------------------------------------
##
##       \   ,__,
##        \  (oo)____
##           (__)    )\
##              ||--||
##
##--------------------------------------------------------------------
### READ DOSCAR ##
f = open('DOSCAR', 'r')
lines = f.readlines()
f.close()
index = 0
natoms = int(lines[index].strip().split()[0])


## define user-input form ##
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)


tokb = str(b)
tokc = str(c)

fb = open("DOS" + tokb, 'r')

fc = open("DOS" + tokc, 'r')

fsum = open("DOS_sum_" + tokb + "+" + tokc, 'w')

for i in range(0, 301):

    if a==1 and b==c:

        lineb = fb.readline().strip().split()
        linec = fc.readline().strip().split()
        posb = np.array([float(j) for j in lineb])
        posc = np.array([float(k) for k in linec])

        fsum.write(str(posb[0]) + str('%15.8f' % (posb[1])) + str('%15.8f' % (posb[3] + posb[5] + posb[7] ))\
        + str('%15.8f' % (posb[9] + posb[11] + posb[13] + posb[15] + posb[17] )) \
        + str('%15.8f' % (posb[1] + posb[3] + posb[5] + posb[7] + posb[9] + posb[11] + posb[13] + posb[15] + posb[17] )) + '\n')

    else:

        if a == 1 and b!=c:

            lineb = fb.readline().strip().split()
            linec = fc.readline().strip().split()
            posb = np.array([float(j) for j in lineb])
            posc = np.array([float(k) for k in linec])

            fsum.write(str(posb[0]) + str('%15.8f' % (posb[1] + posc[1])) + str('%15.8f' % (posb[3] + posb[5] + posb[7] \
            + posc[3] + posc[5] + posc[7])) + str('%15.8f' % (posb[9] + posb[11] + posb[13] + posb[15] + posb[17] + \
            posc[9] + posc[11] + posc[13] + posc[15] + posc[17])) + str('%15.8f' % (posb[1] + posb[3] + posb[5] + \
            posb[7] + posb[9] + posb[11] + posb[13] + posb[15] + posb[17] +posc[1] + posc[3] + posc[5] + \
            posc[7] + posc[9] + posc[11] + posc[13] + posc[15] + posc[17])) + '\n')
        else:

            if a==0:
                lineb = fb.readline().strip().split()
                linec = fc.readline().strip().split()
                posb = np.array([float(j) for j in lineb])
                posc = np.array([float(k) for k in linec])

fsum.close()
fb.close()
fc.close()
