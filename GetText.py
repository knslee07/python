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
