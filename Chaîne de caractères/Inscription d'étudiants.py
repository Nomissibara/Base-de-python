# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 23:11:27 2023

@author: benib

CONSTRAINTS :
    Les noms des étudiants font moins de 50 caractères de long et commencent par une lettre majuscule.
    
INPUT :
    Un nom d’étudiant.
    
OUTPUT :
    Un entier, 1, 2 ou 3, selon que l’étudiant doit aller voir la première, la seconde ou la troisième personne.
"""
nom_etudiant = input()
if (nom_etudiant[0]>= "A") & (nom_etudiant[0]<= "F"):
    print(1)
elif (nom_etudiant[0]>= "G") & (nom_etudiant[0]<= "P"):
    print(2)
else :
    print(3)
    
