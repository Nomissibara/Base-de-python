# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 23:37:21 2023

@author: benib

Votre programme devra lire un nombre décimal, la quantité de ciment nécessaire pour les fondations de votre nouvelle maison, en kilos. Sachant que le ciment n'est vendu qu'en sacs de 60 kilos et que un sac coûte 45 euross, votre programme devra afficher le coût total du ciment.
"""
from math import *
quantite_de_ciment_necessaire = float(input())
print(ceil(quantite_de_ciment_necessaire/60)*45)
