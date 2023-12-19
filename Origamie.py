# -*- coding: utf-8 -*-
"""
L'epaisseur d'une feuille de papier est de 110 micromètres c'est à dire 0,110 millimètres. Si on la plie 15 fois sue elle-même et que l'épaissuer double à chaque fois, quelle sera l'épaissuer final si on l'exprime en centimètres ?

Votre programme devra calculer et afficher cette valeur (qui n'est pas forcément entière).
"""
epaisseur = 0.110 *0.1
for loop in range(15):
    epaisseur *= 2
    
print(epaisseur)
