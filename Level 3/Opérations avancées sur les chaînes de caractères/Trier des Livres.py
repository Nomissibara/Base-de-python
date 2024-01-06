# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 23:05:19 2024

@author: benib

CONSTRAINTS
    Each book title contains a maximum of 100 characters.

INPUT
    The first line contains an integer nbBooks, the number of books.

    The following nbPounds lines each contain a book title.

    Titles contain only capital letters or spaces.

OUTPUT
    All book titles, one title per line, sorted alphabetically.
"""
nbBooks = int(input())
title_of_books = [""]*nbBooks
for index in range(nbBooks):
    title_of_books[index] = input()
title_of_books.sort()
for index in range(nbBooks):
    print(title_of_books[index])
