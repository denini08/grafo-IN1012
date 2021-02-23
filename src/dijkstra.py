from os import name
import pandas as pd
import sys
import csv
import datetime
from sys import argv


# grafo = [[0, 10, 5, 0, 0],
#          [0, 0, 2, 1, 0],
#          [0, 3, 0, 9, 2],
#          [0, 0, 0, 0, 4],
#          [7, 0, 0, 6, 0]]


def min_path(p, visitados):
    min = sys.maxsize

    for i in range(len(p)):
        if p[i] < min and visitados[i] == False:
            min = i

    return min


def dijkstra(grafo, origem):
    # Pega quantidade de vertices e inicializa vetor de prioridades
    p = [sys.maxsize] * len(grafo[0])
    # Vetor que vai guardar os antecessores
    antecessores = [-1] * len(grafo[0])
    p[origem] = 0
    visitados = [False] * len(grafo[0])

    for i in range(len(grafo[0])):
        # Vertice com o menor peso partindo da origem
        v = min_path(p, visitados)
        visitados[v] = True
        # Percorre verificando os vizinhos de v
        for n in range(0, len(grafo[i])):
            if grafo[v][n] > 0 and p[n] > p[v] + grafo[v][n]:
                p[n] = p[v] + grafo[v][n]
                antecessores[n] = v

    return antecessores, p


def main(city1, city2):
    # inializando o dict das cidades
    pos1 = ''
    pos2 = ''
    names = {}
    with open("dict_n.csv", "r") as f:
        reader = csv.DictReader(f)
        # for r in reader:
        #     if r['nome'] == city1:
        #         pos1 = r['posicao']
        #     if r['nome'] == city2:
        #         pos2 = r['posicao']
        #     if pos1 != '' and pos2 != '':
        #         break

        for r in reader:
            names[r['posicao']] = r['nome']

        for k in names.keys():
            if names[k] == city1:
                pos1 = k
            if names[k] == city2:
                pos2 = k
            if pos1 != '' and pos2 != '':
                break

    print(f'posicao cidade1: {pos1}\nposicao cidade2: {pos2}')

    print("Começou a ler matriz!!! ", datetime.datetime.now())

    grafo = pd.read_csv('pesos_100miles.csv', sep=',',
                        header=None).iloc[:, :].values
    print("Terminou leitura de matriz!!! ", datetime.datetime.now())

    antecessores, pesos = dijkstra(grafo, int(pos1))
    antecessor = pos2
    path = []
    path.append(antecessor)

    while antecessor >= 0:
        antecessor = antecessores[antecessor]
        path.append(antecessor)

    print('A menor distância entre a cidade {} e a cidade {} é de {} milhas'.format(
        city1, city2, pesos[pos2]))
    print('\n')
    print('E as cidades que formam esse caminho, são: ')
    print('\n')

    for i in range(path):
        print(names[str(i)])

    exit(0)
    # names = ['s', 't', 'y', 'x', 'z']
    # for i in range(len(caminhos)):
    #     print('A({}) = {}'.format(names[i], names[i]))


if __name__ == "__main__":

    if len(argv) == 3:
        city1 = argv[1]
        city2 = argv[2]
        print(f'cidade 1: {city1}\ncidade 2: {city2}')
        main(city1, city2)
    else:
        print('"Error, use\npython3 dijkstra.py "CITY1" "CITY2"')
        exit(1)
