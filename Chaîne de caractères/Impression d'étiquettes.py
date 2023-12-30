# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 22:51:13 2023

@author: benib

CONSTRAINTS :
    La ligne de texte contiendra toujours moins de 50 caractères.
    
INPUT:
    Une seule ligne de texte.
    
OUTPUT :
    Les caractères du texte, affichés verticalement.
"""
ligne_de_texte = input()
for loop in range(len(ligne_de_texte)):
    print(ligne_de_texte[loop])
