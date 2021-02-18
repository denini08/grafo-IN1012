grafo = [
  {1,3}, #0
  {0,3,4}, #1
  {4},   #2
  {0,1},   #3
  {1,2}  #4
]

for i in range(len(grafo)):
  print(f'{i}:')
  for j in grafo[i]:
    comum = grafo[j] & grafo[i] #interseção
    l = len(comum)
    print(f' é amigo de: {j}, quantidade de amigos em comum: {l}.', end='')
    print(f' Amigos em comum: {comum}' if l>0 else '\n' )


