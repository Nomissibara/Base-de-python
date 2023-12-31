# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 21:18:04 2023

@author: benib

Ce que doit faire votre programme :
    Vous choisissez 2121 comme deuxième mot de passe. Écrivez un programme qui attend successivement les codes 4242 puis 2121, en affichant cette fois « Premier code bon. » entre les deux, comme montré dans l'exemple.

    Ici, écrivez une et une seule fonction pour demander successivement les deux codes.
"""
def mot_de_passe_different(mot_de_passe):
    code_secret = 0
    while code_secret != mot_de_passe :
        print("Entrez le code :")
        code_secret = int(input())
        
mot_de_passe_different(4242)
print("Premier code bon.")
mot_de_passe_different(2121)
print("Bravo.")
