# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 23:25:10 2023

@author: benib

CE QUE DOIT FAIRE VOTRE PROGRAMME :
    Un livre de compte décrit les achats et ventes successives de 10 produits numerotés de 1 à 10. Le livre décrit les opérations depuis une situation oû le stock de chacun des produits était de zéro.
    
    Chaque ligne du livre de comptes décrit l'achat (augmentation du stock) ou la vente (réduction du stock) d'une certaine quantité de l'un des produits.
    
    Votre objectif esr de déterminer pour chaque produit, la quantité restant dans le stock à l'issue de l'ensemble de ces achats et ventes.
    
INPUT :
    La prémiere ligne contient un entier nbOperations : le nombre d'opérations décrites dans le livres de comptes.
    
    Suivent ensuite nbOperations paires d'entiers, oû le premier entier de chaque paire est le numéro de l'ingrédient concerné par l'opération, et le deuxième est la quantité. Si la quantité est négative, l'opération est une vente, et si  elle est positive, l'opération est un achat du produit indiqué.
    
OUTPUT :
    Vous devez afficher 10 entiers sur la sortie : la quantité restante pour chacun des produits dans l'ordre de leur numéro, une fois l'ensemble des opérations décrites dans le livre effectuées.
"""
nbOperations = int(input())
livre_de_comptes = [0]*10
for loop in range(nbOperations):
    indice = int(input())
    quantite = int(input())
    livre_de_comptes[indice] += quantite 
for indices in range(10):
    print(livre_de_comptes[indices])

