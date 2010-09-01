#! /usr/bin/python
#    A program to count the physical lines of a python program
#        mcb3k with help from alm4x    2.12.2k9    v0.5
#          all versions before this were trying to implement all logic lines
#          Goal: by v1.0, count all logic lines, or all phys. lines, user's choice

def physLineCounter(pyScript):
    """takes a python script and returns the number of physical lines of code, including all the comments."""
    
    scriptName = pyScript
    script = open(scriptName) #opens the file for the pyScript
    scriptList = script.readlines() #this splits the entire file into a list of strings.
    numberOfLines = len(scriptList)
    script.close()     

    return numberOfLines

# end of the function

#this is like the main function

myPyScript = raw_input('Hello, and Welcome to pyLineCounter!  Please type the name of the file you want me to process: ')

finalTally = physLineCounter(myPyScript)

print 'Here is the final tally!  The number of lines of code is: ', finalTally
