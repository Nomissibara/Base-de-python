# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 23:55:51 2023

@author: benib

Ce que doit faire votre programme :
    Écrivez un programme qui convertit des valeurs du système métrique en valeurs du système de mesure américain. On fournit des mesures à votre programme, en mètres, grammes ou degrés Celsius et vous devez les convertir respectivement en pieds, livres et degrés Fahrenheit.
    
    Voici les règles de conversion à utiliser :
        - 1 pied = 0,3048 mètres ;
        - 1 gramme = 0,002205 livres ;
        - température en degrés Fahrenheit = 32 + 1,8 × température en degrés Celsius.
    
    On vous donne sur la première ligne le nombre de conversions à effectuer, puis sur les lignes suivantes la valeur à convertir, et son unité : m, g ou c (avec une espace entre les deux).

    Affichez en sortie les valeurs converties, suivies d'une espace et de leur unité : p, l ou f.
    
    Il n'est en fait pas judicieux d'écrire des fonctions pour résoudre cet exercice : le mieux est de définir des constantes. Vous pouvez aussi profiter de cet exercice pour expérimenter l'instruction « selon », switch dans certains langages.

"""
def piedMetre(mettre):
    return mettre*1/0.3048
def grammeLivre(gramme):
    return gramme*0.002205
def fahrenheitCelsius(celsius):
    return 32 + 1.8*celsius
   
nbConversion = int(input())
for loop in range(nbConversion):
    entre = input().split(' ')
    nbr = float(entre[0])
    if (entre[1] == "m"):
        print(piedMetre(nbr), " p")
    if (entre[1] == "g"):
        print(grammeLivre(nbr), " l")
    if (entre[1] == "c"):
        print(fahrenheitCelsius(nbr), " f")
