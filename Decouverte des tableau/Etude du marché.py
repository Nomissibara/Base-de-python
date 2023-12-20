# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 23:51:18 2023

@author: benib

CE QUE DOIT FAIRE VOTRE PROGRAMME :
    On vous donne le numéro du produit préféré par différentes personnes. Ecrivez un programme qui indique pour chaque numéro de produit, le nombre de personnes dont c'est le produit préféré.
    
INPUT :
    les deux premiers entiers à lire sont le nombre total de produits nbProduits et le nombre de personnes nbPersonnes (nbPersonnes <= 1000) ayant exprimé leur souhait.
    
    On lit ensuite nbPersonnes entiers : les numéros des produits préférés des différentes personnes. Les produits sont nulérotés de 0 à nbProduits - 1.
    
OUTPUT :
    Vous devez afficher nbProduits entiers : pour chaque produit dans l'ordre de leur numéro, affichez le nombre de personnes qui le préférent.
"""
nbProduits = int(input())
nbPersonnes = int(input())
produits = [0]*nbProduits
for loop in range(nbPersonnes):
    numeros_de_produits_preferer = int(input())
    produits[numeros_de_produits_preferer] += 1
for loop in range(nbProduits):
    print(produits[loop])

