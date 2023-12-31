# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 21:49:12 2023

@author: benib

Ce que doit faire votre programme :
    Écrivez une fonction nommée min2, qui prend deux entiers en paramètres et retourne le plus petit. Pour démontrer l'utilisation de cette fonction, vous lirez 10 entiers sur l'entrée, utiliserez votre fonction pour conserver uniquement le plus petit des 10, puis vous l'afficherez à la fin.
"""
def min2(valeur1 , valeur2):
    if valeur1 < valeur2:
        return valeur1
    return valeur2
valeur1 = int(input())
minimum = 0
for  loop in range(9):
    valeur2 = int(input())
    minimum = min2(valeur1, valeur2)
    valeur1 = minimum
print(minimum)