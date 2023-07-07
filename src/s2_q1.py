#!/usr/bin/env python3

def fonction(entree: list):
    sortie = []
    for i in range(1,4):
        for j in entree:
            sortie.append(j+str(i))
    print(sortie)

entree = ['A','B','C']
fonction(entree)