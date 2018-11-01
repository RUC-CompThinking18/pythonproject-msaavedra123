'''
The variables s and t represent two of five questions that the user will be asked.'''

s = raw_input("1. In 2017, how many soldiers died in action around the globe? ")
t = raw_input("2. In 2017, how many American died in the United States because of terrorism? ")

'''Def main is to combine all the functions that will be taking place, in the overall program,
this was done because it allows me to see the output of each individual input, or answer to
the questions. Currently, the only issue I have is making Incorrect or correct print after
each question instead of at the end of all
the questions.'''

def main():
	'''for def soldiers(s), s is the user answer for question 1, it is taken as the argument,
	if the answer is correct it will print "correct" if it is incorrect "incorrect" will be printed,
	no particular value will be returned'''
	def soldiers(s):
		s = int(s)
		if s == 21:
			print("Correct")
		elif s != 21:
			print("Incorrect")
	'''def terror(t), works the same way as def soldiers(s), where t is the user input for question
	2 no value is to be returned'''
	def terror(t):
		t = int(t)
		if terror == 4:
			print("Correct")
		elif t != 4:
			print("Incorrect")

	soldiers(s)
	terror(t)
main()
