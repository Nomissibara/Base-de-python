# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 00:00:56 2024

@author: benib

CONSTRAINTS
Tous les titres de livres ainsi que les acronymes contiennent au plus 200 caractères.

CONSTRAINTS
    All book titles and acronyms have a maximum length of 200 characters.

INPUT
    On the first line, an acronym, made up of uppercase letters only.

    On the second line, an integer nbBooks, the number of book titles.

    On the following nbPounds lines, the book titles, consisting solely of letters or spaces, without accents.

    The words of each title are always separated by a single space.

OUTPUT
    You must display each book title corresponding to the acronym, using all lower-case letters except the first letter of each word, which must be capitalized.
"""

acronym = input().lower()
nbBooks = int(input())

for loop in range(nbBooks):
    title_of_books = list(input().lower().split(" "))
    if len(acronym) == len(title_of_books):
        index = 0
        check = True
        while check and index < len(acronym):
            if acronym[index] == list(title_of_books[index])[0] :
                check = True
            else :
                check = False
            index += 1
    else :
        check = False
    if check :
        for index in range(len(title_of_books)):
            title_of_books[index] = list(title_of_books[index])
            title_of_books[index][0] = title_of_books[index][0].upper()
            title_of_books[index] = "".join(title_of_books[index])
            print(title_of_books[index], end =" ")
        print()