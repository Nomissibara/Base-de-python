# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 23:41:50 2023

@author: benib

Ce que doit faire votre programme :
    Écrivez un programme qui affiche une ligne de « X », un rectangle de « # », et un triangle de « @ ». Les deux formes doivent être creuses (remplies avec des espaces).

    L'entrée comporte quatre entiers, un par ligne :
        - le nombre de « X » de la ligne à afficher ;
        - le nombre de lignes du rectangle de « # » ;
        - le nombre de colonnes du rectangle ;
        - le nombre de lignes du triangle de « @ ».
        
    Vous devez afficher les trois formes successivement, avec une ligne blanche entre chaque forme, comme le montre l'exemple.
    
    Votre objectif doit être d'obtenir le code source le plus simple et clair possible, en le décomposant en fonctions.
"""
def afficheLigne(caractere  , longueur):
    for loop in range(longueur):
        print(caractere , end = "")
   
def afficheColonne(caractere  , longueur):
    for loop in range(longueur):
        print(caractere)

def afficheEspace(caractere , ligne):
    print(caractere , end= "")
    afficheLigne(" ", ligne-2)
    print(caractere , end= "")

def afficheRectangle(motif, ligne , colonne):
    if (ligne==1):
        afficheLigne(motif , colonne)
    elif (colonne == 1):
        afficheColonne(motif, ligne)
    else :
        afficheLigne(motif, colonne)
        print()
        for loop in range(ligne-2):
           afficheEspace(motif, colonne)
           print()
        afficheLigne(motif , colonne)

def afficheTriangle(caractere , nbLignes):
    print(caractere)
    for loop in range(nbLignes-2):
        afficheEspace("@", loop+2)
        print()
    afficheLigne("@", nbLignes)
      
longueur1 = int(input())
ligne1 = int(input())
colonne = int(input())
ligne2 = int(input())
afficheLigne("X", longueur1)
print()
print()
afficheRectangle("#", ligne1 , colonne)
print()
print()
afficheTriangle("@", ligne2)
