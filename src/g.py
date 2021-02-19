import csv


def ver_amigos(n):
    amigos_n = set()
    for i in range(len(grafo2[n])):
        if grafo2[n][i] > 0:
            amigos_n.add(i)
    return amigos_n


grafo2 = [[0, 1, 0, 1, 0],
          [1, 0, 0, 1, 1],
          [0, 0, 0, 0, 1],
          [1, 1, 0, 0, 0],
          [0, 1, 1, 0, 0]]

grafo2 = []
for a in range(4039):
    grafo2.append([])
    for b in range(4039):
        grafo2[a].append(0)

with open('facebook_combined.txt', 'r') as f:
    lines = f.readlines()
    for l in lines:
        aux = l.split(' ')
        a = int(aux[0])
        b = int(aux[1])
        grafo2[a][b] = 1
        grafo2[b][a] = 1


del lines

grafo3 = []
for a in range(4039):
    grafo3.append([])
    for b in range(4039):
        grafo3[a].append(0)

# debugger
#grafo2 = grafo2[:30]
# for l in range(len(grafo2)):
#    grafo2[l] = grafo2[l][:30]

with open('pontos.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(grafo2)

for i in range(len(grafo2)):
    print(i)
    for j in range(len(grafo2[i])):
        if grafo2[i][j] > 0:
            amigos_i = ver_amigos(i)
            amigos_j = ver_amigos(j)
            comum = len(amigos_i & amigos_j)  # interceção
            grafo3[i][j] = comum


with open('pesos.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(grafo3)
