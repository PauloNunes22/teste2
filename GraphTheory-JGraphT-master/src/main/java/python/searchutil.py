# -*- coding: utf-8 -*-
"""searchutil.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uvGh8yK5oqpcJ3cUrzK8MDYbbenky_9W

Este notebook contém funções para busca em árvore.

O código pode ser importado em seu notebook usando o seguinte comando:

!wget https://raw.githubusercontent.com/pdlmachado/GraphTheory-JGraphT/master/src/main/java/python/searchutil.py

Testes para as funções encontram-se neste notebook:

https://colab.research.google.com/drive/1lxpFEmuvvAN-0jMwQ6djRzEqFwyXWGF0?
"""

# Se desejar compilar, descomente o(s) comando(s) abaixo
#!pip install jgrapht

# Importando a JgraphT 
from random import randint
from jgrapht import create_graph

"""# Busca em Largura"""

# Retorna uma árvore de busca em largura
# Algoritmo BFS visto nas notas de aula, retornando árvore ao invés da função predecessor
# Retorna uma árvore orientada, a função nível e a função tempo

def bfs (g,root):
  if not root in g.vertices:
    return None,None,None
  i = 0
  Q = [] # Lista que representa a fila Q
  i = i+1
  visited = [root] # Lista com vértices que foram pintados
  l = {}
  l[root] = 0
  t = {}
  t[root]=i
  Q = [root]
  tree = create_graph(directed=True,weighted=False,dag=True)
  tree.add_vertex(root)
  while Q != []:
    x = Q[0] # x é o vértice da cabeça de Q
    neighbors = [g.opposite(e,x) 
                  for e in g.edges_of(x) if g.opposite(e,x) not in visited]
    if neighbors != []: # x ainda tem vizinhos não pintados
      # escolhe um dos vizinhos y aleatoriamente
      y = neighbors[randint(0,len(neighbors)-1)]
      i = i+1
      visited.append(y)
      tree.add_vertex(y)
      tree.add_edge(x,y)
      l[y] = l[x]+1
      t[y] = i
      Q.append(y) #adiciona y ao fim da fila
    else:
      Q.pop(0) # remove x da cabeça da fila Q
  return tree,l,t

"""# Busca em Profundidade"""

# Constroi uma árvore de busca em profundidade
# Algoritmo DFS apresentado nas notas de aula
# Retorna uma árvore DFS orientada e as funções tempo
def dfs (g,root):
  if not root in g.vertices:
    return None,None,None
  f = {} # função tempo de inclusão na árvore
  t = {} # função tempo de saída da pilha
  i = 0
  S = [] # Lista que representa a pilha S
  i = i+1
  visited = [root] # Lista com vértices que foram pintados
  f[root] = i
  S.append(root)
  tree = create_graph(directed=True,weighted=False,dag=True)
  tree.add_vertex(root)
  while S != [] :
    x = S[0] # x é o topo da pilha S
    neighbors = [g.opposite(e,x) for e in g.edges_of(x) if g.opposite(e,x) not in visited]
    i = i+1
    if neighbors != []:
      # escolhe um dos vizinhos y aleatoriamente
      y = neighbors[randint(0,len(neighbors)-1)]
      visited.append(y)
      tree.add_vertex(y)
      tree.add_edge(x,y)
      f[y] = i
      S.insert(0,y) #adiciona y ao topo de S
    else:
      t[x] = i
      S.pop(0) #remove x do topo
  return tree,f,t