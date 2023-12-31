# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 22:14:38 2023

@author: benib

Ce que doit faire votre programme :
    Votre programme doit afficher les termes de la suite qui succèdent à celui fourni sur l'entrée, séparés par des espaces, jusqu'à ce que le nombre 1 soit atteint.
    
    Important : 
        vous devez utiliser une fonction qui prend un terme en paramètre, et retourne le suivant.
"""
def suite_de_colatz(nombre):
    while nombre != 1 :
        if nombre%2 == 0 :
            nombre = nombre//2
            print(nombre, end = " ")
        else  :
            nombre= nombre*3 + 1
            print(nombre, end = " ")
nb = int(input())
suite_de_colatz(nb)

"""
def termeSuivant(terme):
   if terme % 2 == 0:
      return terme // 2
   else:
      return terme * 3 + 1
terme = int(input())
while terme != 1:
   terme = termeSuivant(terme)
   print(terme, end = " ")
print()
"""
