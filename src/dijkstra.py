# import pandas as pd
# arr = pd.read_csv('pesos.csv', sep=',').iloc[:, :].values

import sys


grafo = [[0, 10, 5, 0, 0],
          [0, 0, 2, 1, 0],
          [0, 3, 0, 9, 2],
          [0, 0, 0, 0, 4],
          [7, 0, 0, 6, 0]]


def min_path(p, visitados):
    min = sys.maxsize

    for i in range(len(p)):
        if p[i] < min and visitados[i] == False:
            min = i

    return min

def dijkstra(grafo, origem):
    p = [sys.maxsize] * len(grafo[0]) #Pega quantidade de vertices e inicializa vetor de prioridades
    antecessores = [-1] * len(grafo[0]) #Vetor que vai guardar os antecessores
    p[origem] = 0 
    visitados = [False] * len(grafo[0])

    for i in range(len(grafo[0])):
        v = min_path(p, visitados) #Vertice com o menor peso partindo da origem
        visitados[v] = True
        for n in range(0,len(grafo[i])): #Percorre verificando os vizinhos de v
            if grafo[v][n] > 0 and p[n] > p[v] + grafo[v][n]:
                    p[n] = p[v] + grafo[v][n]
                    antecessores[n] = v

    return antecessores


caminhos = dijkstra(grafo,0)
names = ['s','t','y','x', 'z']
for i in range(len(caminhos)):
    print('A({}) = {}'.format(names[i], names[i]))




        




    





