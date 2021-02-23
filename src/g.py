# este codigo demora cerca de 45 minutos para executar
import csv
import codecs

com = []
# lendo o BD e salvando em um dict
with open('sf12010placedistance100miles.csv', 'r') as f:
    lines = f.readlines()
    for n, l in enumerate(lines):
        if n == 0:
            continue
        l = l.replace('"', '').replace('\n', '')
        aux = l.split(',')
        a = aux[1]
        b = aux[4]
        dis = float(aux[2])
        dic = {'a': a, 'b': b, 'dis': dis}
        com.append(dic)


del lines
del f

# criando as posicoes na matrix para cada cidade
count_cidades = -1
dic_cidades = {}
for n, c in enumerate(com):
    if c['a'] not in dic_cidades:
        count_cidades += 1
        dic_cidades[c['a']] = count_cidades
    if c['b'] not in dic_cidades:
        count_cidades += 1
        dic_cidades[c['b']] = count_cidades


# salvando um csv onde cada linha contem o id do banco, posicao na matrix e nome da cidade
reader = csv.DictReader(codecs.open('sf12010placename.csv', 'r',  encoding='utf-8',
                                    errors='ignore'))
impresso = set()
with open('dict_n.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['id', 'posicao', 'nome'])
    for nomes in reader:
        for k in dic_cidades.keys():
            nome = nomes['place']
            if k == nome and k not in impresso:
                impresso.add(k)
                writer.writerow([k, dic_cidades[k], nomes['placename']])

del impresso
del reader

# criando a matrix
print('tamanho %d' % (len(dic_cidades)))
# exit(0)

grafo2 = []
for a in range(len(dic_cidades)):
    grafo2.append([])
    for b in range(len(dic_cidades)):
        grafo2[a].append(0)

# preenchendo a matrix

for c in com:
    posicao_a = dic_cidades[c['a']]
    posicao_b = dic_cidades[c['b']]
    grafo2[posicao_a][posicao_b] = c['dis']
    grafo2[posicao_b][posicao_a] = c['dis']


# salvando a matrix
with open('pesos_100miles.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(grafo2)
