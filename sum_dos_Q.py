#!/usr/bin/env python

##--------------------------------------------------------------------
##
##                code writen on 08 Oct. 2019, by Qing W
##                        qing.wang@outlook.fr
##
## Hint: This code can make sum of DOS for atoms in a specific range of
##       pre-split DOS (by using previous split_dos_Q.py code) -> usage:
##       sum_dos_Q.py [0] [start] [end]; or sum of DOS for two separately
##       labeled atoms (or for one atom)'
##       number-> usage: sum_dos_Q.py [1] [a] [b]
##
##--------------------------------------------------------------------
##
##       \   ,__,
##        \  (oo)____
##           (__)    )\
##              ||--||
##
##--------------------------------------------------------------------

print("Usage: [0] [start] [end] \n   Or  [1] [i] [j]")
print("Please enter 3 numbers (separate them with whitespace): ")



## define usage ##
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

## set variables ###

tokb = str(b)
tokc = str(c)

fb = open("DOS" + tokb, 'r')
fc = open("DOS" + tokc, 'r')

linesb = fb.readlines()
linesc = fc.readlines()

fsum1 = open("DOS_sum_" + tokb + "+" + tokc, 'w')

fsum0 = open("DOS_sum_" + str(b) + " to " + str(c), 'w')

## for DOS sum of two separately labeled atoms

if a == 1 and b != c:

    for k in range(0, 301):

        posb = linesb[k].strip().split()
        posc = linesc[k].strip().split()

        fsum1.write(str(float(posb[0])) + str('%15.8f' % (float(posb[1]) + float(posc[1]))) + \
        str('%15.8f' % (float(posb[2]) + float(posb[3]) + float(posb[4]) + float(posc[2]) + float(posc[3]) + float(posc[4]))) \
        + str('%15.8f' % (float(posb[5]) + float(posb[6]) + float(posb[7]) + float(posb[8]) + float(posb[9])\
        + float(posc[5]) + float(posc[6]) + float(posc[7]) + float(posc[8]) + float(posc[9]))) \
        + str('%15.8f' % (float(posb[1]) + float(posb[2]) + float(posb[3]) + float(posb[4]) + float(posb[(5)]) + \
        float(posb[6]) + float(posb[7]) + float(posb[8]) + float(posb[9]) + float(posc[1]) + float(posc[2]) + \
        float(posc[3]) + float(posc[4]) + float(posc[5]) + float(posc[6]) + float(posc[7]) + float(posc[8]) + float(posc[9]))) + '\n')


## for the case where the target DOS is the DOS of one single atom
elif a==1 and b==c:

    for k in range(0, 301):

        posb = linesb[k].strip().split()

        fsum1.write(str(float(posb[0])) + str('%15.8f' % (float(posb[1]))) + \
        str('%15.8f' % (float(posb[2]) + float(posb[3]) + float(posb[4]))) \
        + str('%15.8f' % (float(posb[5]) + float(posb[6]) + float(posb[7]) + float(posb[8]) + float(posb[9]))) \
        + str('%15.8f' % (float(posb[1]) + float(posb[2]) + float(posb[3]) + float(posb[4]) + float(posb[5]) + \
        float(posb[6]) + float(posb[7]) + float(posb[8]) + float(posb[9]))) + '\n')

## sum of DOS for several atoms in a specific range

elif a==0 and b!=c:

    for k in range(0, 301):
        sum1 = 0
        sum2 = 0
        sum3 = 0
        sum4 = 0

        for i in range(b, c + 1):

            tok = str(i)
            f0 = open("DOS" + tok, 'r')
            lines = f0.readlines()
            pos = lines[k].strip().split()

            sum1 = sum1 + float(pos[1])
            sum2 = sum2 + float(pos[2]) + float(pos[3]) + float(pos[4])
            sum3 = sum3 + float(pos[5]) + float(pos[6]) + float(pos[7]) + float(pos[8]) + float(pos[9])
            sum4 = sum4 + float(pos[1]) + float(pos[2]) + float(pos[3]) + float(pos[4]) + float(pos[5]) + float(pos[6]) + \
            float(pos[7]) + float(pos[8]) + float(pos[9])
        f0.close()

        fsum0.write(str(float(pos[0])) + str('%15.8f' % (sum1)) + str('%15.8f' % (sum2)) + str('%15.8f' % (sum3)) + str('%15.8f' % (sum4)) + '\n')

fsum0.close()
fsum1.close()

fb.close()
fc.close()
