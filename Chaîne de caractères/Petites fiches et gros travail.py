# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 23:01:27 2023

@author: benib

CONSTRAINTS :
    Il y a toujours 6 titres de livres (et donc 6 noms d’auteurs) sur chaque fiche.
    
    Les titres de livres et les noms d’auteurs font toujours moins de 200 caractères de long.
    
INPUT :
    Pour chacun des 6 livres, une ligne contenant le nom de l’auteur, et une ligne contenant le titre du livre.
    
OUTPUT :
    Pour chacun des livres, vous devez afficher sur une ligne le titre du livre, puis sur la ligne suivante le nom de l’auteur.
"""
for loop in range(6):
    nom_de_auteur = input()
    titre = input()
    print(titre)
    print(nom_de_auteur)
    
