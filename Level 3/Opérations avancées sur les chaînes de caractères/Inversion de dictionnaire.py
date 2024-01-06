# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 23:15:53 2024

@author: benib

INPUT
    The first line contains the integer nbWords.

    The following nbWords lines each contain two words separated by a space: one word in the first language and one word in the second.

    The words contain no spaces and are all lowercase letters.

    Word pairs are sorted according to the alphabetical order of the words in the first language.

OUTPUT
    You should see all inverted word pairs (first the word in the second language, then the word in the first) sorted in alphabetical order by the words in the second language.
"""
nbBooks = int(input())
pairs_of_Word = [""] * nbBooks
for idpairs in range(nbBooks):
   first , second = input().split(" ")
   pairs_of_Word[idpairs] = second + " " + first
pairs_of_Word.sort()
for idpairs in range(nbBooks):
   print(pairs_of_Word[idpairs])
