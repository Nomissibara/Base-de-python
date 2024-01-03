# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 23:10:31 2024

@author: benib

CONSTRAINTS :
    Le nom de l’auteur comprend au plus 50 caractères.
    
INPUT :
    Sur la première ligne, le nom de l’auteur, la première lettre étant une majuscule.
    
    Sur la seconde ligne, l’âge de son fils aîné au moment où le livre a été écrit.
    
OUTPUT :
    Le numéro du bâtiment et la lettre correspondant à l’allée, sur la même ligne sans espace entre les deux.
"""
def Livre(nom, age):
   print(ord(nom[0])-ord("A") + 1, end="")
   print(chr(age + ord("A") -1))
def main():
   nom = input()
   Age = int(input())
   Livre(nom,Age)
main()
