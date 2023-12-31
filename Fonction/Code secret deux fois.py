# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 20:47:27 2023

@author: benib

Ce que doit faire votre programme :
    Le mot de passe que vous choisissez est 4242. Écrivez un programme qui attend ce code une première fois, en le demandant de manière répétée par une ligne contenant « Entrez le code : », puis qui une fois ce code entré, affiche « Encore une fois. » et attend le code à nouveau, avant d'afficher « Bravo. » et de se terminer (vous trouverez sans doute cela plus clair avec l'exemple ci-dessous).
    
    L'objectif de cet exercice est d'utiliser une fonction pour éviter de recopier deux fois les instructions qui permettent d'attendre le code 4242.
"""
def mot_de_passe(secret_code):
    while secret_code != 4242 :
        print("Entrez le code :")
        secret_code = int(input())

print("Entrez le code :")
secret_code = int(input())
mot_de_passe(secret_code)
print("Encore une fois.")
print("Entrez le code :")
secret_code1 = int(input())
mot_de_passe(secret_code1)
print("Bravo.")