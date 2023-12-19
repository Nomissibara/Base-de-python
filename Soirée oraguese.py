# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 23:58:26 2023

@author: benib

Votre programme devra lire un decimal, le temps (en secondes) entre le moment où vous voyez l'eclair et le moment où vous entendez le tonnerre. Il devra calculer et afficher la distance entre vous et l'orage, arrondi au kilomètre près.

On supposera que la lumière se deplace instantanément. La vitesse du son dépend de paramètres comme l'altitude, la temperature... mais on supposera qu'en cette soirée elle vaut 340,29mètre/seconde.
"""
from math import *
temps = float(input())
print(round((340.29*temps)/1000))
