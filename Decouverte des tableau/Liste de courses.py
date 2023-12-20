# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 23:15:53 2023

@author: benib

Il y a 10 ingédients et ils ont tous un prix au kilo différent : 9,5,12,15,7,42,13,10,1 et 20.

Votre programme devra lire 10 entiers, le poids (en kilogramme) qu'il faut acheter pour chaque ingrédient. Il devra calculer le coût total de ces achats.
"""
prix_au_kilo = [9,5,12,15,7,42,13,10,1,20]
total = 0
for loop in range(10):
    poids = int(input())
    total += prix_au_kilo[loop]*poids
print(total)
