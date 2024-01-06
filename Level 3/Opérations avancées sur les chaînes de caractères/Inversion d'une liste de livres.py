# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 22:57:00 2024

@author: benib

CONSTRAINTS
    Each book title contains a maximum of 100 characters.

INPUT
    The first line contains an integer nbBooks, the number of books.

    The following nbBooks lines each contain a book title.

    Books are sorted from least to most interesting.

OUTPUT
    All book titles, one title per line, sorted from most interesting to least interesting.
"""

nbBooks = int(input())
list_of_books = [""]*nbBooks
for index in range(nbBooks):
    list_of_books[index] = input() 
for index in range(nbBooks-1 , -1 , -1):
    print(list_of_books[index])