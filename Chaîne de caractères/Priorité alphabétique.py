# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 23:14:37 2023

@author: benib

CONSTRAINTS :
    Chaque nom est composé uniquement de lettres majuscules, sans espaces.
    
    Sa longueur sera au plus égale à 50.
    
INPUT :
    Sur la première ligne, le nom de la première personne.
    
    Sur la seconde ligne, le nom de la seconde personne.
    
OUTPUT :
    Le nom le plus petit selon l’ordre alphabétique, c’est-à-dire le nom qui vient en premier selon cet ordre.
    
    Si les deux noms sont égaux, il ne faut rien afficher car la personne a voulu tricher en faisant deux demandes d’un seul coup.
"""
nom1 = input()
nom2 = input()
if nom1 < nom2 :
    print(nom1)
elif nom1>nom2 :
    print(nom2)    