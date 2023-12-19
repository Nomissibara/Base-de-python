# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 22:58:21 2023

@author: benib

Votre programme doit d'abord lire le nombre de légumes mis en vente. Ensuite, pour chacun, il doit lire 3 nombres décimaux : son poids, son àge (en nombre de jours depuis la ceuillette), et son prix de vente. Votre programme doit ensuite afficher pour chaque légume son prix au kg (au fur et à mesure que les légumes sont présentés).
"""

nbLegumes = int(input())
for loop in range(nbLegumes):
    poids = float(input())
    age = float(input())
    prix_de_vente = float(input())
    print(prix_de_vente/poids)
