# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 21:34:08 2023

@author: benib

Ce que doit faire votre programme :
    Votre programme doit lire la longueur de la dentelle, puis l'afficher sous la forme de trois lignes remplies respectivement de « X », de « # » et de « i ».
"""

def ligneCaractères(caractère, longueur):
   for iCol in range(longueur):
      print(caractère, end = "")
   print()
longueur_de_la_dentelle = int(input())
ligneCaractères("X",longueur_de_la_dentelle)
ligneCaractères("#",longueur_de_la_dentelle)
ligneCaractères("i",longueur_de_la_dentelle)