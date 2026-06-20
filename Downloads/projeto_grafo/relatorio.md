# Relatório do Projeto

## 1. Domínio Escolhido

O projeto modela uma rede de cidades ligadas por estradas.

Os vértices representam cidades e as arestas representam estradas entre elas.

O grafo é não direcionado, pois uma estrada pode ser percorrida nos dois sentidos.

As arestas possuem peso correspondente à distância em quilômetros.

## 2. Representação do Grafo

Foi utilizada uma lista de adjacência.

A escolha foi feita porque essa estrutura possui menor consumo de memória em grafos esparsos, onde cada cidade se conecta apenas a algumas outras cidades.

Enquanto a matriz de adjacência exige espaço proporcional a V², a lista de adjacência utiliza espaço proporcional a V + E.

## 3. Busca em Largura (BFS)

Foi implementada a busca em largura.

O algoritmo utiliza uma fila para visitar os vértices por níveis.

No contexto do projeto, a BFS permite descobrir todas as cidades alcançáveis a partir de uma cidade inicial e verificar conectividade.

## 4. Caminho Mínimo

Foi utilizado o algoritmo de Dijkstra.

O objetivo é encontrar a rota de menor distância entre duas cidades.

O resultado representa o trajeto mais curto em quilômetros.

## 5. Árvore Geradora Mínima

Foi utilizado o algoritmo de Kruskal.

A árvore geradora mínima conecta todas as cidades utilizando a menor soma possível de distâncias.

Esse tipo de solução é utilizado em problemas reais de infraestrutura, telecomunicações e logística.

## 6. Aplicações Reais

Sistemas de GPS utilizam algoritmos de caminho mínimo para calcular rotas.

Empresas de logística utilizam grafos para otimizar entregas.

Redes de computadores e telecomunicações também empregam conceitos semelhantes para reduzir custos de conexão.

## 7. Limitações

Em grafos muito grandes, com milhões de vértices e arestas, o processamento pode se tornar mais lento e exigir técnicas avançadas de armazenamento e paralelização.
