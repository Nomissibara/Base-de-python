# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 23:22:38 2023

@author: benib

CONSTRAINTS :
    Le titre et le nom de l’auteur font chacun moins de 100 caractères.
    
    Ils ne contiennent que des lettres majuscules et des espaces.
    
INPUT :
    Sur la première ligne, le titre du livre.
    
    Sur la seconde ligne, le nom de l’auteur.
    
OUTPUT :
    Sur la première ligne, le titre du livre, sans aucune voyelle, ni espace.
    
    Sur la seconde ligne, le nom de l’auteur, sans aucune voyelle, ni espace.
"""
titre_du_livre = input()
nom_de_auteur = input()
for indice in range(len(titre_du_livre)):
    if not((titre_du_livre[indice] == "A") or (titre_du_livre[indice] == "E") or (titre_du_livre[indice] == "U") or (titre_du_livre[indice] == "I") or (titre_du_livre[indice] == "O") or (titre_du_livre[indice] == "Y") or (titre_du_livre[indice] == " ")):
        print(titre_du_livre[indice], end="")
print()
for indice in range(len(nom_de_auteur)):
    if not((nom_de_auteur[indice] == "A") or (nom_de_auteur[indice] == "E") or (nom_de_auteur[indice] == "U") or (nom_de_auteur[indice] == "I") or (nom_de_auteur[indice] == "O") or (nom_de_auteur[indice] == "Y") or (nom_de_auteur[indice] == " ")):
        print(nom_de_auteur[indice], end="")        
print()