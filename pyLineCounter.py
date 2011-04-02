#! /usr/bin/python
#    A program to count the lines of a python program
#        mcb3k with help from alm4x    4.2.2k11    v0.6
#          Goal: by v1.0, count all logic lines, or all phys. lines, user's choice

def physLineCounter(pyScript):
    """takes a python script and returns a list of physical lines of code, including all the comments."""
    
    scriptName = pyScript
    script = open(scriptName) #opens the file for the pyScript
    scriptList = script.readlines() #this splits the entire file into a list of strings.
    numberOfLines = len(scriptList)
    script.close()     

    return [numberOfLines]

# end of the function

def logicalLineCounter(pyScript):
	"""Takes a python script and returns the number of logical lines of code, the number of comments, and the number of physical lines of code in a list."""

	#Lets do open up the file, push it into a list, and close the file
	scriptName = pyScript 
	script = open(scriptName)
	scriptList = script.readlines()
	scipt.close()

	lineCount = len(scriptList) #set lineCount to the length physical lines
	commentCount = 0

	for each in scriptList:
		if not 0 == scriptList[each].count(';')
			lineCount = lineCount + scriptList[each].count(';') #if the physical line contains a semicolon, i.e. contains multiple statements.
			if scriptList[each].endswith(';') == True
				lineCount = lineCount - 1 #because it's already been counted, right?
		if scriptList[each].startswith("#") == True
			lineCount = lineCount - 1
			commentCount = commentCount + 1
		
		#Count all lines that contain a '#'and add one to commentCount
		if scriptList[each].count('#') == True and scriptList[each].startswith("#") != True
			commentCount = commentCount + 1

	return [lineCount, commentCount, len(scriptList)]

#this is like the main function

myPyScript = raw_input('Input file name: ')
countType = raw_input('Physical or Logical lines: ')

while countType.capitalize() != "Physical" or countType.capitalize() != "Logical"
	if countType.capitalize() == "Physical"
		tallies = physLineCounter(myPyScript)

	elif countType.capitalize() == "Logical"
		tallies = logicalLineCounter(myPyScript)
	else 
		print "That wasn't a valid input!"

for each in tallies
	print tallies[each]
