# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 23:23:05 2023

@author: benib

CONSTRAINTS :
    La longueur de chaque titre de livre et de chaque résumé n'excèdera jamais 1000 caractères.
    
INPUT :
    Sur la première ligne, un entier nbLivres, le nombre total de livres.
    
    Sur la deuxième ligne, un entier longueurMinimale, la longueur minimale acceptable pour un résumé de livre.
    
    Les 2 * nbLivres lignes suivantes contiennent, de manière alternée, un titre de livre et le résumé associé.
    
OUTPUT :
    Vous devez afficher, à raison d’un par ligne, le titre des livres dont le résumé n'est pas assez long, c'est-à-dire dont la longueur n'est pas au moins égale à longueurMinimale.
"""
nbLivres = int(input())
longueurMinimale = int(input())
for loop in range(nbLivres):
    titre_du_livre = input()
    resume_associe = input()
    if len(resume_associe) < longueurMinimale:
        print(titre_du_livre)
