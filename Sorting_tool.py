#!/usr/bin/env python

##--------------------------------------------------------------------
##
##                code writen on 09 Oct. 2019, by Qing W
##                        qing.wang@outlook.fr
##
## Hint: Personal code to add numeric labels on every lines of one
##       file, for facililitating the R plotting   
##
##--------------------------------------------------------------------
##
##       \   ,__,
##        \  (oo)____
##           (__)    )\
##              ||--||
##
##--------------------------------------------------------------------


with open("file1", "r") as a, open("sorted-file.txt", "w") as b:
    index = 1
    for line in a:
        b.write("{:4d} {}\n".format(index, line.rstrip()))
        index += 1

print("file 'sorted-file.txt' is directly readable by R now! ")
