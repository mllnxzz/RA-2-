# Lucas Palacio Bertoncello

# Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  criar  um  programa,  utilizando  a
# linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irá  apresentar  os  resultados  de
# operações que serão realizadas entre dois conjuntos de dados.
# O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt)
# contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
# em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
# segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
# operações  que  estão  descritas  no  arquivo,  este  número  de  operações  será  um  inteiro;  as  linhas
# seguintes  seguirão  sempre  o  mesmo  padrão  de  três  linhas:  a  primeira  linha  apresenta  o  código  da
# operação  (U para união, I para interseção, D para diferença e C produto cartesiano),  a  segunda  e
# terceira linhas conterão os elementos dos conjuntos separados por virgulas.

# Importação do arquivo de texto
arquivo = open('info1.txt', 'r')
linhas = arquivo.readlines()

# Função específica para remover números repetidos de um array
def remove_duplicados(array):
  clean = []

  for i in array:
    if i not in clean:
      clean.append(i)

  return clean

# Função para calcular cada expressão
def conjuntos(c1, c2, c):
  conjunto = []

  # União
  if c == 'U':
    for i in range(len(c1)):
      conjunto.append(c1[i])
    for i in range(len(c2)):
      conjunto.append(c2[i])

  # Plano Cartesiano
  if c == 'C':
    for i in range(len(c1)):
      for d in range(len(c2)):
        conjunto.append(f'({c1[i]}, {c2[d]})')

  # Diferença
  if c == 'D':
    for i in c1:
      if i not in c2:
        conjunto.append(i)

  # Intersecção
  if c == 'I':
    for i in range(len(c1)):
      for d in range(len(c2)):
        if c1[i] == c2[d]:
          conjunto.append(c1[d])

  return sorted(conjunto)

# Rodando um loop sobre cada linha do arquivo
operacoes = []
print('')
for i in range(len(linhas)):
  linha = linhas[i].strip()

  if linha == 'U' or linha == 'I' or linha == 'D' or linha == 'C':
    c1 = linhas[i + 1].strip().split(', ')
    c2 = linhas[i + 2].strip().split(', ')
    operacoes.append(linha)
    if linha == 'U':
      print(f'União: conjunto 1 {c1}, conjunto 2 {c2}: {remove_duplicados(conjuntos(c1, c2, linha))}')
      print('')
    if linha == 'I':
      print(f'Interseção conjunto 1 {c1}, conjunto 2 {c2}: {remove_duplicados(conjuntos(c1, c2, linha))}')
      print('')
    if linha == 'D':
      print(f'Diferença conjunto 1 {c1}, conjunto 2 {c2}: {conjuntos(c1, c2, linha)}')
      print('')
    if linha == 'C':
      print(f'Plano cartesiano conjunto 1 {c1}, conjunto 2 {c2}: {conjuntos(c1, c2, linha)}')
      print('')

# Exibição da quantidade de operações
total = len(remove_duplicados(operacoes))
print(f'{total} operações realizadas.')
print('')
