# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 22:27:00 2023

@author: benib

Ce que doit faire votre programme :
    Écrivez une fonction qui prend en paramètre les coordonnées (x1,y1)
 et (x2,y2)
 de deux points et retourne la distance euclidienne entre ces deux points. On rappelle que la distance euclidienne entre deux points est égale à :
     
     Utilisez ensuite cette fonction dans un programme qui lit quatre nombres décimaux x1
, y1
, x2
 et y2
 tapés au clavier, puis affiche la distance entre les deux points correspondants.
 
 On pourra utiliser la fonction mathématique sqrt(x) qui retourne la racine carrée du paramètre x et qui s'importe avec cette ligne :
"""
from math import*
def distance_euclidienne(x1,y1,x2,y2):
    return sqrt((x2-x1)**2 + (y2 - y1)**2)
x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
print(distance_euclidienne(x1, y1, x2, y2))
