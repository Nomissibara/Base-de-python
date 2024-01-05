# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 22:04:11 2024

@author: benib

FEATURES
    The line of text contains less than 10,000 characters.

INPUT
    A single line of text, not containing accented letters, but which may contain punctuation marks or numbers.

OUTPUT
    For each letter of the alphabet, its frequency of appearance in the text is displayed on one line, defined as the number of times the letter is present, divided by the total number of letters in the text (not the total number of characters).
"""

line_of_text = input().upper()
line_of_text = list(line_of_text)
number_occurence = [0]*26
for loop in range(len(line_of_text)):
    if not(line_of_text[loop].isupper()) :
        line_of_text[loop] = " "
line_of_text = "".join(line_of_text)
line_of_text = "".join(line_of_text.split())
for loop in range(len(line_of_text)):
    index_letter = ord(line_of_text[loop]) - ord("A")
    number_occurence[index_letter] += 1
for loops in range(26):
    print(number_occurence[loops]/len(line_of_text))