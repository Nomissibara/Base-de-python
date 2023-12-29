# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 23:37:10 2023

@author: benib

CONSTRAINTS :
    Chaque nom et prénom est au plus de longueur 100 et ne contient pas d'espace.
    
INPUT :
    Sur la première ligne, un entier nbPersonnes : le nombre total de personnes concernées.
    
    Sur chacune des nbPersonnes suivantes, un prénom et un nom, séparés par une espace.
    
OUTPUT :
    Pour chaque personne, vous devez écrire sur la même ligne son nom, puis son prénom, séparés par une espace.
"""
nbPersonnes = int(input())
for loop in range(nbPersonnes):
    nom_et_prenom = input().split(" ")
    print("{} {}".format(nom_et_prenom[1], nom_et_prenom[0]))
    
# Variante possible
"""
nbPersonnes = int(input())
for loop in range(nbPersonnes):
    prenom, nom = input().spllit(" ")
    print("{} {}".format(nom , prenom))
"""