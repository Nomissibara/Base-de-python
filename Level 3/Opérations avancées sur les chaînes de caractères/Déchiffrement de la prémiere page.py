# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 00:47:34 2024

@author: benib

Dans ce système de cryptage, on remplace chaque lettre du message par une autre, à l'aide d'une grille de cryptage. Pour décrypter le message, il suffit de faire pareil mais avec la grille inverse (la grille de décryptage) et on retrouvera le texte original.

Vous avez plusieurs idées pour cette fameuse clé de décryptage mais comme il serait trop long de tester à la main, vous décidez d’écrire un programme pour décoder automatiquement un texte, étant donnée la clé.

CONSTRAINTS
    Le texte crypté contient au plus 1000 caractères.

INPUT
    La première ligne de l'entrée contient la grille de décryptage, composée de 26 caractères minuscules. La première lettre correspond à la lettre par laquelle il faut remplacer tous les 'a' du texte crypté, la deuxième tous les 'b', etc.

    La deuxième ligne de l'entrée contient le texte crypté.

    Il n’y a pas d’accents, mais il peut y avoir des espaces, de la ponctuation, etc.

OUTPUT
    Vous devez afficher une ligne sur la sortie : le texte décrypté.

    Chaque lettre cryptée doit être remplacée par la lettre décryptée. Les autres caractères (ponctuation, '_', espaces, chiffres), sont laissés tels quels.

    Vous devez respecter la casse : si une lettre était en majuscule (ou minuscule), elle doit le rester !
"""

secret_key = input()
secret_text = input()
for index in range(len(secret_text)):
    if (secret_text[index] >= 'a' and secret_text[index] <= "z") :
        print(secret_key[ord(secret_text[index]) - ord("a")], end = "")
    elif (secret_text[index] >= 'A' and secret_text[index] <= "Z") :
        print(secret_key[ord(secret_text[index]) - ord("A")].upper(), end = "")
    else:
        print(secret_text[index], end = "")