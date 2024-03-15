# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 22:51:34 2024

@author: benib
"""
def c_to_t(chaine):
    tableau = [[int(val) if val != '_' else 0 for val in ligne.split(',')] for ligne in chaine.strip().split('\n')]
    return tableau


def donneSommetDistances(graphe, distance , tstTraite):
    """
    Fonction qui donne le prochain sommet à relier. Ce sommet ne doit pas encore avoir été traité et il doit être a distance minimale des sommets déja traités
    
    - Graphe : la matrice d'adjacence du graphe
    -Distance : Distance de chaque sommet aux sommet traités
    -tstTraite : Liste booleenes qui dit si un sommet est traité ou non

    """
    minimale = float("Inf")
    for v in range(len(graphe)):
        if distance[v] < minimale and not tstTraite[v]:
            minimale = distance[v]
            min_index = v 
    return min_index


def prim(graphe):
    """
    Fonction qui permet d'obtenir la liste des arcs correspondant à l'arbre couvrant gràce à l'algorithme de prim
    - Graphe : La matrice d'adjacence'


    """
    graphe = c_to_t(graphe)
    distances = [float("Inf")]*len(graphe)
    distances[0] = 0
    parent = [None]*len(graphe)
    tstTraite = [False]*len(graphe)
    parent[0] = -1
    
    for _ in range(len(graphe)):
        u = donneSommetDistances(graphe, distances, tstTraite)
        tstTraite[u] = True
        for v in range(len(graphe)):
            if distances[v] > graphe[u][v] > 0 and not tstTraite[v]:
                distances[v] = graphe[u][v]
                parent[v] = u
    return parent

graphe = '''_,14,10,19,_,_,_
14,_,_,15,18,_,_
10,_,_,26,_,29,_
19,15,26,_,16,17,21
_,18,_,16,_,_,9
_,_,29,17,_,_,25
_,_,_,21,9,25,_
'''

print(len(graphe))
parent = prim(graphe)
sommeMax = 0
somme = 0
graphe= c_to_t(graphe)
print("Liste des arcs couvrants minimum")
for i in range(1,len(graphe)):
    print(parent[i], "-", i , "\t", graphe[i][parent[i]])
    somme += graphe[i][parent[i]]
for indec in range(len(graphe)):
    sommeMax += sum(graphe[indec])
print(sommeMax//2 - somme)
    
