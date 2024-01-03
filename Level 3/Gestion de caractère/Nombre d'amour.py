# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 23:19:45 2024

@author: benib

CONSTRAINTS :
    First names are up to 50 characters long.
    
INPUT:
    First names of both children (in uppercase), separated by a space.
    
OUTPUT:
    On a single line, the love numbers of each of the two children.
"""
def convert(prenom):
    prenom = list(prenom)
    for loop in range(len(prenom)):
        prenom[loop] = ord(prenom[loop]) - 65
    return prenom
def somme(prenom):
    somme_de_nombre = 0
    for loop in range(len(prenom)):
        somme_de_nombre += prenom[loop]
    while somme_de_nombre >= 10 :
        nbLove = 0
        somme_de_nombre = list(str(somme_de_nombre))
        for loop in range(len(somme_de_nombre)):
            nbLove += int(somme_de_nombre[loop])
        somme_de_nombre = nbLove
    return somme_de_nombre

first_name1, first_name2 = input().split(" ")
first_name1 = convert(first_name1)
first_name2 = convert(first_name2)
print("{} {}".format(somme(first_name1),somme(first_name2)))


