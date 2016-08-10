#!/usr/bin/env python3
# HW06_ch09_ex02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
#   - name your function print_no_e
##############################################################################
# Imports
import os

# Body
def has_no_e(input_word):
    for letter in input_word:
        if 'e' in input_word:
            return False
    return True
            
 
def print_no_e():
    count = 0
    total = 0
    with open('words.txt', 'r') as f
        lines = f.readlines()
    for word in lines:
        if has_no_e(word):
            count += 1
            total += 1
            print(word.strip())
        else:
            total += 1

    percentage = count/total*100
    print('\n'+"Percentage of words without 'e': ", percentage, "%")
    
        
##############################################################################
def main():
    pass  # Call your function(s) here.
    print_no_e()

if __name__ == '__main__':
    main()
