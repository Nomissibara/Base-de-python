# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 00:23:46 2024

@author: benib

CONSTRAINTS
Each book title has a maximum length of 100.

INPUT
The first line contains an integer nbBooks, the total number of books.

Each of the following nbPounds lines contains a book title.

Titles are composed of spaces and uppercase or lowercase letters, unaccented.

OUTPUT
You need to display every book title that is a palindrome.

To determine whether a title is a palindrome, neither the spaces nor the case (upper or lower case) of the letters will be considered.
"""

nbBooks = int(input())
for loop in range(nbBooks):
    title_of_book = input()
    title_of_book2 = title_of_book.upper()
    title_of_book2 = "".join(title_of_book2.split())
    check  = True
    begin = 0
    end = len(title_of_book2) - 1
    while (begin < end):
        if title_of_book2[begin] != title_of_book2[end]:
            check = False
        begin += 1
        end -= 1
    if check :
        print(title_of_book)
    
    