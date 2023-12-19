# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 23:08:16 2023

@author: benib

Votre prgramme doit d'abord lire un premier entier, qui décrit le nombre de notes obtenues. Ensuite, il doit lire chacune de ces notes, qui sont également des nombres entiers. Enfin, il doit afficher la moyenne de toutes ces notes.
"""

nombre_de_note_obtenues = int(input())
note_final = 0
for loop in range(nombre_de_note_obtenues):
    note = int(input())
    note_final += note
print(note_final/nombre_de_note_obtenues)