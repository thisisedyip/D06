#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou: [type here]
#   - # of words that use all aeiouy: [type here]
##############################################################################
# Imports

# Body
def uses_all(word, string_set):

    if set(word.lower()) >= string_set:
    	return True

def vowel_check():
	with open('Words.txt', 'r') as f:
		lines = f.readlines()

	string = input("Give string: ")
	string_set = set(string)
	count = 0

	for word in lines:
		if uses_all(word, string_set):
			count += 1
			print(word.strip())
	print("There are", count, "words that use the letters", list(string.strip(',')))

##############################################################################
def main():
    pass  # Call your function(s) here.
    vowel_check()
    
if __name__ == '__main__':
    main()

