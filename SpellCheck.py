# Author: Derrick Joyce
# 8/2/2020
# Needs SpellCheck.txt
dictionary = set()

def read_file():
	global dictionary
	if dictionary:
		return
	with open("SpellCheck.txt","r") as f:
		contents= f.read()
	
	dictionary = set(
		word.lower()
		for word in contents.splitlines()
		)
		
def spellcheck(word):

		word = word.lower()
		read_file()
		return word in dictionary
