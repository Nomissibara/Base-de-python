# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 23:15:35 2023

@author: benib

Votre programme devra lire un entier, la population actuelle de la ville, puis un nombre décimal, la croissance prévue de le population, en pourcentage. Il devra alors afficher la nouvelle population de la ville sous la forme d'un nombre entier. On considérera, par convention, qu'une population de 31,4 habitants signifie qu'il y a 31 habotants, on ne compte donc que les habitants entiers !
"""
from math import *

population_actuelle = int(input())
croissance = float(input())
print(floor(population_actuelle + (population_actuelle*croissance)/100))