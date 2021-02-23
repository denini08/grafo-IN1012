# Grafo cidades (IN1012)
Projeto da disciplina de algoritmos II (3a Atividade Teórica)

## Códigos
[`src/g.py`](./src/g.py) -> faz o pre-processamento da base criando a matrix (pesos_100miles.csv) e criando um arquivo que serve como dicionario com o nome da cidade e sua posição na matrix (dict_n.csv). Você não precisa rodar este script, pois a matrix e o dicionario já foram criados.

[`src/dijkstra.py`](./src/dijkstra.py) -> roda o algormitmo de Dijkstra e retorna o menor caminho e as cidades compõem o caminho. 

## Execução

Antes de executar baixe o [arquivo da matrix](https://drive.google.com/file/d/1p5Y2Ep0dZ6kQiZ2ROq9exn0mPbpbSXFa/view?usp=sharing) e o coloque em `/src`
Para executar o algoritmo, use:
```
python3 dijkstra.py "CITY1" "CITY2"
```
Para saber os nomes das cidades veja o arquivo [sf12010placename.csv](src/sf12010placename.csv).
## Alunos
* [Denini Gabriel](https://denini08.github.io/)
* [Matheus Ferreira](https://github.com/matheus-felipe)

## Links externos
* [Link para Slides](https://docs.google.com/presentation/d/1Tg4uo7qjrGbVJOtmG9SGtZiH7fyPHDDXRpcbAT8V3UY/edit?usp=sharing)
* [Link para apresentação em Video](https://youtu.be/5EuNWYcEz2A)
