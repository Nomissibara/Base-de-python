# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 23:52:30 2024

@author: benib

CONSTRAINTS
    The text of the speech contains no more than 10,000 characters.

    Each word has a maximum length of 50.

INPUT
    On the first line, a word. On the second line, the text of the speech.

    There is no punctuation; words and text are made up solely of unaccented letters and spaces. As usual, "word" means a sequence of characters containing no spaces.

OUTPUT
    You must indicate how many times the given word is present in the speech text.

    Whatever the case of the word you're given, or of its appearances in the text, you must count them all!
"""
word = input().upper()
speech = list(input().upper().split(" "))
count = 0
for loop in range(len(speech)):
    if word == speech[loop]:
        count += 1
print(count)
