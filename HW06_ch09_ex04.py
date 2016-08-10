#!/usr/bin/env python
# HW06_ch09_ex04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1: Local oaf
#       2: Leach hole
#       3: Loofah off
##############################################################################
# Imports

# Body
def uses_only(word, string_list):
#    user_word = input("Provide a word: ")
#    user_string = input("Provide a string of letters: ")
#    string_list = list(user_string)

#    print(string_list)
#    print(user_word)

    for letter in word:
        if letter not in string_list:
            return False
    return True

def sentence_time(user_string):
    with open('Words.txt', 'r') as f:
        lines = f.readlines()
    
    string_list = list(user_string)
    for word in lines:
        if uses_only(word.strip(), string_list):
            print(word.strip())
            

##############################################################################
def main():
    pass  # Call your function(s) here.
    sentence_time("acefhlo")
    
if __name__ == '__main__':
    main()
