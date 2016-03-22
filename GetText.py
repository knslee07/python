# GetTextData.py
""" This module provides functions that can be
used to extract data from text files.
.py file should be in the same folder as the text file.
"""

def fileToStringList(FName):
    """ Returns a list of strings L with the property that
    L[k] is the kth line in the file with name FName
    
    PreC: FName is a string that names the file that is to be read.
    It should include the suffix, i.e., MyFile.txt.
    The file must be in the current working directory.
    """
    L = []
    with open(FName,"r") as F:
        for s in F:
            # Remove trailing newline character...
            s1=s.rstrip("\n")
            # Remove trailing carraige return...
            s2 = s1.rstrip("\r")
            # Append this "cleaned up" file line...
            L.append(s2)
    return L


def stringToWordList(s):
    """Returns t.split() where t is obtained from s.lower() by replacing
    every non-letter in this string with a blank. Basically, it returns
    a list of the words in s.
    
    PreC: s is a string.
    """
    t = ''
    for c in s.lower():
        if c in 'abcdefghijklmnopqrstuvwxyz':
            t = t + c
        else:
            t = t + ' '      
    return t.split()



# ShowGetData.py

""" This module illustrates how to use the functions in
GetData.py to count the number of lines, words, and chracters in
a text file.
"""

from GetData import fileToStringList, stringToWordList

# Create a list os strings that house all the data in a text file...
NameOfFile = 'PridePrej.txt'
L = fileToStringList(NameOfFile)

# Note that len(L) is the number of lines in the file.
nLines = len(L)

# nChars = the number of characters 
nChars = 0

# nWords = the number of words
nWords = 0

for s in L:
    nChars += len(s)
    nWords += len(stringToWordList(s))

print '\nFile : %s \n' % NameOfFile     
print 'Number of lines       = %7d' % nLines
print 'Number of words       = %7d' % nWords
print 'Number of characters  = %7d' % nChars





# ShowCounties.py
""" Sample computations with the US Census dataset that was downloaded from
  
  http://www.census.gov/popest/data/counties/totals/2014/CO-EST2014-alldata.html
  
The dataset is slightly modified and is in the file CensusData.csv

If c is a line in that file and v = c.split(',') then here are some
definitions:

   v[5]   State Name
   v[6]   County Name
   v[7]   2010 county population
   v[10]  2011 county population
   v[11]  2012 county population
   v[12]  2013 county population
   v[13]  2014 county population
"""
 
from GetData import fileToStringList
TheCounties = fileToStringList('CensusData.csv')

# Total population
pop = 0;
for c in TheCounties:
    v = c.split(',')
    pop+=int(v[7])
print "\nUSA Population in 2010 = %1d\n" % pop

# The county with the biggest percentage growth in population...
growthMax = 0
for c in TheCounties: # c is the each line in the CSV file.
    v = c.split(',') # v becomes a list of elements of c, each line of CSV.
    growth = float(v[13])/float(v[7]) # growth rate between 2013 and 2010.
    if int(v[7])>=100000 and growth>growthMax:
        growthMax = growth
        vMax = v
print vMax[6],vMax[5],'grew by',int(growthMax*100),'percent'
