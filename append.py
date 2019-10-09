#!/usr/bin/env python


##--------------------------------------------------------------------
##
##                code writen on 08 Oct. 2019, by Qing W
##                        qing.wang@outlook.fr
##
## Hint: a code to append all separated files contents from multi-calculations
##       into a new file (like XDATCAR) 
##      
##--------------------------------------------------------------------
##
##       \   ,__,
##        \  (oo)____
##           (__)    )\
##              ||--||
##
##--------------------------------------------------------------------


## change the files names below (or add/delete more files) with your target files needed to be appended ##

filenames = ['file1', 'file2','file3','file4']


## all files contents will be stored in a file named "appended_file" ##

with open('appended_file', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())
            
print("All your files : ", filenames, "are successfully appended into new file 'appended_file' ! ")


