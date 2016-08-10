#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function called is_abecedarian that returns True if the letters in a
# word appear in alphabetical order (double letters are ok).
#   - write is_abecedarian
# (2)
# How many abecedarian words are there?
#   - write additional function(s) to assist you
#   - number of abecedarian words: 596
##############################################################################
# Imports

# Body
def is_abecedarian(word):
    word_list = list(word)
    word_sort = sorted(word_list)
    if word_list == word_sort:
        return True

def abecedarian_count():
    with open("words.txt", "r") as f:
        lines = f.readlines()
        
    count = 0
    
    for word in lines:
        if is_abecedarian(word.strip()):
            count += 1
    print(count)

##############################################################################
def main():
    pass  # Call your function(s) here.
    abecedarian_count()

if __name__ == '__main__':
    main()
