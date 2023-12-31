# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 21:42:36 2023

@author: benib

Ce que doit faire votre programme :
    Votre programme doit lire le nombre de lignes et de colonnes de la feuille, puis le motif à afficher sous la forme d'un caractère. Il doit alors afficher le motif de sorte qu'il remplisse chaque cellule de la feuille.
"""
def remplir_feuille(ligne , colonne , motif):
    for iligne in range(ligne):
        for icol in range(colonne):
            print(motif , end = "")
        print()

lignes = int(input())
colonnes = int(input())
motif = input()
remplir_feuille(lignes, colonnes, motif)