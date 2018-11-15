'''
Was unable to figure out how to construct a class, so have five separate functions instead.
The variables p, s, t, h, o and c represent each of the six questions the user will be answering. '''

'''for def planes(), p is the user answer for question 1,  if the answer is correct it will print "correct."
If answer is a letter instead of a number or incorrect, will print incorrect with error message and reprint the question so the user.
For each answer it will be checking for a string and not an int because of unexpected errors.'''

def planes():
	print("Please enter whole numbers only to answer each question.")
	p = raw_input("1. How many citizens were killed in plane crashes in 2017? ")
	if p == "13":
		print("Correct")
	else:
		print("Incorrect, make sure to enter a whole number!")
def soldiers():
	s = raw_input("2. In 2017, how many soldiers died in action around the globe? ")
	if s == "21":
		print("Correct")
	else:
		print("Incorrect, make sure to enter a whole number!")
		#s = raw_input("2. In 2017, how many soldiers died in action around the globe? ")
def terror():
	t = raw_input("3. In 2017, how many American died in the United States because of terrorism? ")
	if t == "4":
		print("Correct")
	else:
		print("Incorrect, make sure to enter a whole number!")
		#t = raw_input("3. In 2017, how many American died in the United States because of terrorism? ")
def shooter():
	h = raw_input("4. How many people were killed by mass shooters in 2017? ")
	if h == "428":
		print("Correct")
	else:
		print("Incorrect, make sure to enter a whole number!")
		#h = raw_input("4. How many people were killed by mass shooters in 2017? ")
def chicago():
	c = raw_input("5. How many deaths were caused by Chicago's 'top gangs' in 2017? ")
	if c == "675":
		print("Correct")
	else:
		print("Incorrect, make sure to enter a whole number!")
		#c = raw_input("5. How many deaths were caused by Chicago's 'top gangs' in 2017? ")
def police():
	o = raw_input("6. In 2017, how many people were killed by police? ")
	if o == "1147":
		print("Correct")
	else:
		print("Incorrect, make sure to enter a whole number!")
		#o = raw_input("6. In 2017, how many people were killed by police? ")

planes()
soldiers()
terror()
shooter()
chicago()
police()
''' Plan to print names of various police brutality victims names were located in a database from https://policeviolencereport.org/
Main article located: https://www.theroot.com/heres-how-many-people-police-killed-in-2017-1821706614 , it summarizes all data but includes links to the main
sources'''
