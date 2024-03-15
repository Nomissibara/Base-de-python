# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 22:56:19 2024

@author: benib

Votre centre de tri sépare les déchets collectés suivant leur type : papier, carton, verre, etc. Une fois triés, les déchets sont vendus à des sociétés qui se chargent de les réutiliser comme matières premières ou pour produire de l'énergie. Une société est ainsi chargée du traitement des produits très polluants comme les batteries, piles et autres produits chimiques. Une fois par semaine, un camion de cette entreprise passe pour ramasser ces déchets. Il arrive cependant que le camion ne puisse pas emporter l'ensemble de vos déchets et que vous deviez les stocker, parfois plusieurs semaines.

Pour éviter d'avoir à stocker trop longtemps ces produits polluants, avec les risques que cela comporte, vous décidez de vous débarasser en priorité des éléments les plus dangereux.

Vous disposez de bacs contenant divers produits dangereux. Sur chaque bac est inscrite une valeur qui indique à quel point le contenu de ce bac est polluant (une valeur élevée correspond à un produit très polluant). On vous indique le nombre de bacs M que le camion peut transporter.

Lorsque le camion arrive, un robot va chercher dans le stock le bac le plus polluant qui s'y trouve, le place dans le camion, puis recommence l'opération jusqu'à avoir un camion rempli de M bacs.

Écrivez un programme qui affiche les niveaux de polluants des bacs dans l'ordre dans lequel le robot les place dans le camion.

CONSTRAINTS
    1 <= N <= 5 000, où N est le nombre de bacs de votre stock.
    0 <= P <= 108, où P est le niveau de polluant d'un bac.
    1 <= M <= 500, où M est le nombre de bacs que le camion peut transporter.
    M <= N 
INPUT
    La première ligne de l'entrée contient deux entiers séparés par un espace : le nombre N de bacs du stock et le nombre M de bacs pouvant être transportés par le camion.

    La deuxième ligne contient N entiers séparés par des espaces : le niveau de pollution de chacun des bacs de votre stock.

OUTPUT
    Vous devez écrire une ligne sur la sortie, contenant M entiers séparés par des espaces : le niveau de pollution des M bacs placés dans le camion, dans l'ordre où le robot les a sortis du stock.
"""

N , M = map(int, input().split())
N_integer = input()
N_integer = list(map(int, N_integer.split(" ")))
N_integer.sort()
index = 1
while index <= M:
    print(N_integer[-index], end = " ")
    index += 1