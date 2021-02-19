# for i in range(len(grafo)):
#   print(f'{i}:')
#   for j in grafo[i]:
#     comum = grafo[j] & grafo[i] #interseção
#     l = len(comum)
#     print(f' é amigo de: {j}, quantidade de amigos em comum: {l}.', end='')
#     print(f' Amigos em comum: {comum}' if l>0 else '\n' )

grafo = [
  {1,3}, #0
  {0,3,4}, #1
  {4},   #2
  {0,1},   #3
  {1,2}  #4
]

grafo2 = [[0,1,0,1,0],
          [1,0,0,1,1],
          [0,0,0,0,1],
          [1,1,0,0,0],
          [0,1,1,0,0]]

for i in range(0,len(grafo2[0])):
  comum = 0
  for c in range(0, len(grafo2)):
    if grafo2[i][c] > 0:
      for z in range(0, len(grafo2[c])):
        if grafo2[i][z] > 0 and grafo2[c][z]:
          comum += 1
      print("{} é amigo de {}. Eles tem {} amigos em comum".format(i, c, comum))
