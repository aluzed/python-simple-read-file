# Read file sample
# Author : Alexandre PENOMBRE <aluzed@gmail.com>

# read a file, line by line
with open('file.txt') as fp:
    for line in fp:
        print line[:-1] # do not get the end of line \n
