# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 23:24:36 2024

@author: benib

CONSTRAINTS
Text line contains less than 10,000 characters.

INPUT
A single line of text, consisting only of unaccented lowercase or uppercase letters and spaces.

We guarantee that in all tests, only one letter is the most used, so there are no ties.

OUTPUT
You must display a line on the output, containing the letter of the alphabet most present in the text supplied as input.

For each letter, you must count both its uppercase and lowercase occurrences, but display the result in uppercase. Spaces are ignored.
"""

text_input = input().upper()

text_input = "".join(text_input.split())
number_occurence = [0]*26
index = 0
for idCaractere in range(len(text_input)):
    index_letter = ord(text_input[idCaractere]) - ord("A")
    number_occurence[index_letter] += 1
    if number_occurence[index_letter] > number_occurence[index] :
        index = index_letter
print(chr(index + ord("A")))
        
