#!/usr/bin/env python

##--------------------------------------------------------------------
##
##                code writen on 10 Oct. 2019, by Qing W
##                        qing.wang@outlook.fr
##
## Hint: This is a tool for converting the the XDATCAR file (the one
##       contains the MD itinerary info) to a .xyz format file, which
##       is more applicable to VMD visualize tool (could avoid VMD
##       crashes)
##
##--------------------------------------------------------------------
##
##       \   ,__,
##        \  (oo)____
##           (__)    )\
##              ||--||
##
##--------------------------------------------------------------------

## read the XDATCAR file ##

f = open("XDATCAR", 'r')

xyz = open("Itinerary_XDA.xyz", 'w')

## skip the empty line ##
comment = f.readline()

## read lattice parameters ##
factor = f.readline().strip().split()
a = float(f.readline().strip().split()[0])
b = float(f.readline().strip().split()[1])
c = float(f.readline().strip().split()[2])

atom_types = f.readline().strip().split()
atom_numbers = f.readline().strip().split()

## assign element type to atomic numbers by dict ##
dict = {}
j = 0
tot_N = 0
for i in range(len(atom_types)):
    dict[atom_types[i]] = int(atom_numbers[j])
    tot_N = int(atom_numbers[j]) + tot_N
    j = j +1


while len(f.readline()) > 0:
    xyz.write(str(tot_N)+' '+'\n')
    xyz.write("a comment line"+'\n')

## itinerary by atomic number ##
    for key in atom_types:
        for k in range(dict[key]):

            coord = f.readline().strip().split()
            xyz_a = float(coord[0])*a
            xyz_b = float(coord[1])*b
            xyz_c = float(coord[2])*c
            xyz.write(str(key)+str('%15.8f' % (xyz_a))+str('%15.8f' % (xyz_b))+str('%15.8f' % (xyz_c))+'\n')
xyz.close()
f.close()


