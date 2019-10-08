#!/usr/bin/env python

import numpy as np
import pandas as pd

##--------------------------------------------------------------------
##   code writen on 20 sept 2019, by Qing W
##            qing.wang@outlook.fr
##
## This only works for spin-polarized DOS calc. (LORBIT = 11, ICHARGE= 11)
## The fermi-lever has been returned to zero in this code
## Hint: This code will split the DOS for every atom in the system from
##       DOSCAR, and named as DOS0 (the total dos for all atoms),
##       DOS1 (dos for atom number 1), DOS2 (dos for atom 2),ect...
##--------------------------------------------------------------------
##
##       \   ,__,
##        \  (oo)____
##           (__)    )\
##              ||--||
##
##--------------------------------------------------------------------


### READ DOSCAR ##
#Mark the atoms number and fermi energy, number of dos points informatons###

f = open('DOSCAR', 'r')
lines = f.readlines()
print(type(lines))
f.close()
index = 0
natoms = int(lines[index].strip().split()[0])
index = 5
nedos = int(lines[index].strip().split()[2])
efermi = float(lines[index].strip().split()[3])
print("WARNING: only tested for 'vasp.4.*', LORBIT=11, Spin polarized calc, use with caution! " )
print("There are",natoms,"atoms in system")
print("Fermi lever is",efermi,"eV")

### write DOS0 ####
with open("DOS0","w+") as writer0:
    for i in range(6,307):
        e = float(lines[i].strip().split()[0])
        e_ef = e - efermi
        writer0.writelines('%15.8f'%(e_ef))
        ### it means write down the "e" content by keeping 8 valid numbers with total 15 empty space###

### here loop in loop, for the second loop, it will run all possibility(statements) firstly,
        # then will return to first loop, then try all possibily in second loop agin###
        for j in range(1,5,2):
            tot = float(lines[i].strip().split()[j])
            writer0.writelines('%15.8f'%(tot))
        writer0.write('\n')
writer0.close()

#### write DOSi#####

for i in range(1,natoms+1):
    tok = str(i)
    fdos = open("DOS"+tok, 'w')
    for i in range(307+i+301*(i-1), 307+i+301*i):
        en = float(lines[i].strip().split()[0])
        en_ef = en - efermi
        fdos.writelines('%15.8f' % (en_ef))

        for j in range(1,19,2):
            line = float(lines[i].strip().split()[j])
            fdos.writelines('%15.8f' % (line))
        fdos.write('\n')
fdos.close()
