# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 23:14:45 2023

@author: benib

CE QUE DOIT FAIRE VOTRE PROGRAMME :
    On vous décrit les charettes qui composent une caravane, en vous donnant pour chacune, le poids des marchandises qu'elle transporte.
    
    Votre programme doit déterminer quel poids ajouter ou rétirer à chaque charette, pour qu'elles transportent toutes ensuite le même poids, et ce sans modifier le poids total transporté par l'ensemble des charettes de la caravane.
    
INPUT :
    L'entrée commence par un entier nbCharrettes (nbCharrettes <= 3000) : le nombre de charrettes de la caravane.
    
    Les nbCharrettes lignes suivantes décrivent chacune une charrette par un nombre décimal : le poids qu'elle transporte initialement.
    
OUTPUT :
    Vous devez afficher nbCharrettes nombres décimaux sur la sortie : le poids à ajouter à chaque charrette (ce qui revient à en retirer si ce nombre est négatif), dans le même ordre que celui de l'entrée. Il n'y a pas d'arrondis à faire.
"""
nbCharrettes = int(input())
poids_marchandises = [0]*nbCharrettes
poids_total = 0
for indice in range(nbCharrettes):
    poids_marchandises[indice] = float(input())
    poids_total += poids_marchandises[indice]
for indices in range(nbCharrettes):
    print(poids_total/nbCharrettes - poids_marchandises[indices])
