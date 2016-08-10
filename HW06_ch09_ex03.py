#!/usr/bin/env python3
# HW06_ch09_ex03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write forbidden_prompt and
#   - modify to create forbidden_param that accepts the string as an argument
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters: find_five
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports
import os
import collections
import string

# Body

def avoids(user_word, string_list):
    """ return True if word NOT forbidden"""
    for letter in user_word:
        if letter in string_list:
            return False
    return True
                

def forbidden_prompt():
    """ print count of words NOT forbidden by input"""
    count = 0
    with open('Words.txt', 'r') as f:
        lines = f.readlines()

    user_string = input("Please provide a string of characters: ")
    string_list = list(user_string)
    
    for word in lines:
        if avoids(word, string_list):
            count += 1
    print(count)
                   


def forbidden_param(param):
    """ return count of words NOT forbidden by param"""
    count = 0
    with open('Words.txt', 'r') as f:
        lines = f.readlines()

    string_list = list(param)

    for word in lines:
        if avoids(word, string_list):
            count+= 1
    print(count)


def find_five():
    alphabet = string.ascii_lowercase
    alphabet_set = set(alphabet)
    
    with open('Words.txt', 'r') as f:
        text = f.read()

    counts = collections.Counter(c for c in text if c in alphabet_set)
    counts_list = []
    for letter in alphabet:
        counts_list.append([counts[letter], letter])
    counts_list.sort()
    print("The 5 forbidden letters that will yield the least amount of words are: ", end='') 
    for a, b in counts_list[:5]:
        print(b, end='')
    print()
        


##############################################################################
def main():
    find_five()
    # Your final submission should only call five_five

if __name__ == '__main__':
    main()
