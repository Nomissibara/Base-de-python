# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 23:10:50 2024

@author: benib

All the books that interest him are lined up on a shelf. Each month, this person picks up the first book on the shelf, then the second and so on until the end. However, she will only read a book if its title is located, in alphabetical order, after each of the books she has read during the month. If not, she removes the book from the shelf, without reading it.

Given the list of possible book titles for the following month, given in the order they appear on the shelf, you need to determine which ones she will read.


CONSTRAINTS
    Each book title will contain a maximum of 100 characters.

INPUT
    On the first line, an integer nbPounds, the total number of books.

    The following nbPounds lines each contain a book title.

    Titles may only contain capital letters or spaces.

OUTPUT
    The list of titles respecting the rule given in the statement.
"""

nbLivres = int(input())
Livres = [""]*nbLivres
teste = ""
for loop in range(nbLivres):
    Livres[loop] = input()
for indice in range(nbLivres):
    if Livres[indice] >= teste :
        teste = Livres[indice]
        print(Livres[indice])