# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 00:23:02 2023

@author: benib

Ce que doit faire votre programme :
    
    Le premier entier à lire est le nombre de participants (au plus 3 000) qui sera toujours pair. Ensuite il faut lire, pour chaque participant, un entier qu'il a choisi librement.
    
    Les équipes sont constituées ainsi : la personne ayant choisi le plus petit entier est avec celle ayant choisi le plus grand, celle ayant choisi le deuxième plus petit est avec celle ayant choisi le deuxième plus grand, et ainsi de suite.
    
    Vous devrez afficher la composition de chacune des équipes, dans l'ordre : d'abord celle dont le plus petit numéro fait partie, puis celle dont le second plus petit numéro fait partie, et ainsi de suite. Au sein de chaque équipe on affichera d'abord le plus petit numéro puis le plus grand.
    
    On vous garantit que tous les numéros sont différents.
"""
nbParticipant = int(input())
tableau_de_correspondance = [0]*nbParticipant
for indice in range(nbParticipant):
    tableau_de_correspondance[indice] = int(input())
tableau_de_correspondance.sort()
debut = 0
fin = nbParticipant-1
for indice in range(int(nbParticipant/2)):
    print("{} {}".format(tableau_de_correspondance[debut], tableau_de_correspondance[fin]))
    debut +=1
    fin -= 1