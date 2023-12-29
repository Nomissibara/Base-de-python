# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 23:43:26 2023

@author: benib

CE QUE DOIT FAIRE VOTRE PROGRAMME :
Il devra lire un premier entier, le nombre d'habitants (au plus 1000) puis, pour chaque habitant il devra lire sa fortune, un entier. Il devra calculer puis afficher une valeur permettant de dire facilement si une personne est riche ou pas, simplement en regardant si la fortune de cette personne est plus grande ou plus petite que cette valeur.

Deux cas peuvent présenter :
    ¤ Si le nombre d'habitants est impair, par exemple si leur fortunes sont 10, 5, 12, 8, 3 alors la valeur recherchéé est 8. En effet, il y aura alors 2 personne "riche" (10 et 12), 2 "moins riches" (3 et 5) et 1 juste au milieu (8) qui ne donnera ni recevra de cadeau.
    ¤ Si le nombre d'habitants est pair, par exemple si leurs fortunes sont 10,5,12,8,3,9 alors la valeur recherchée est entre 8 et 9. Il y a en effet 3 personne "riches" (9,10,12) et 3 "moins riche" (3,5 et 8). Par convention on prendra la valeur 8.5, c'est à dire la moyenne de 8 et 9.
"""
nombre_habitants = int(input())
fortune = [0]*nombre_habitants
for indice in range(nombre_habitants):
    fortune[indice] = int(input())
fortune.sort()
if nombre_habitants % 2 == 0:
    print((fortune[int(nombre_habitants/2)] + fortune[int(nombre_habitants/2 -1)])/2)
else :
    print((fortune[nombre_habitants//2]))
