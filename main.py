# Importação de bibliotecas necessárias
import pandas as pd                             # Para manipulação de dados em tabelas
import networkx as nx                           # Para criação e visualização de grafos
import matplotlib.pyplot as plt                 # Para plotar gráficos
import ast                                      # Para converter strings em listas reais
from collections import Counter                 # Para contar frequências de bandas
from networkx.drawing.layout import bipartite_layout  # Para layout bipartido automático

# Dados: nomes dos alunos e suas bandas favoritas (listas como strings)
data = {
    "nome": [
        "Luis Gustavo Dias Frigeri", "Marcos Vinicius", "Luiz Otávio Vieira Martins Guimarães",
        "Lucas Pereira", "Vitor", "João Celso da Silva Nogueira dos Santos",
        "Vinicius Oliveira", "Jonathan", "Portaluppi", "Rafael", "Luiz Felipe",
        "Karol", "Nicolas Augusto Cardoso", "Luiz Antônio Marcussi Neto",
        "Kaio Enrique", "Kendy H."
    ],
    "bandas": [
        "['phonk', 'rock', 'heavy metal']",
        "['sabaton', 'iron maiden', 'insomnium']",
        "['charlie brown jr', 'jota quest', 'rosa de saron']",
        "['link do zap', 'gp da zl', 'joji']",
        "['menos e mais', 'israel e rodolfo', 'kendrick lamar']",
        "['linking park', 'pink floyd', 'megadeath']",
        "['bringmethehorizon', 'novulent', 'signcrushesmotorist']",
        "['bee gees', 'backstreet boys', 'west life']",
        "['marino', 'the neighbourhood', 'twenty one pilots']",
        "['linkin park', 'system of a down', 'bruno e marrone']",
        "['nirvana', 'gorillaz', 'ac/dc']",
        "['slipknot', 'raimundos', 'charlie brown jr.']",
        "['projeto sola', '5 a seco', 'attos 2']",
        '["guns nroses", "legiao urbana", "beatles"]',
        "['system of down', 'slipknot', 'linkin park']",
        "['iron maiden', 'linkin park', 'imagine dragons']"
    ]
}

# Criação do DataFrame com os dados
df = pd.DataFrame(data)

# Conversão das strings de listas para listas reais de bandas
df['bandas'] = df['bandas'].apply(ast.literal_eval)

# Junta todas as bandas em uma única lista
todas_bandas = [banda for lista in df['bandas'] for banda in lista]

# Conta quantas vezes cada banda aparece
contagem = Counter(todas_bandas)

# Seleciona apenas as bandas que aparecem em 2 ou mais listas (populares)
bandas_populares = {banda for banda, freq in contagem.items() if freq >= 2}

# Criação do grafo bipartido (não direcionado)
G = nx.Graph()

# Adiciona nós e arestas ao grafo apenas para bandas populares
for _, row in df.iterrows():
    pessoa = row['nome']
    bandas = set(row['bandas']).intersection(bandas_populares)  # Filtra apenas bandas populares
    if bandas:
        G.add_node(pessoa, bipartite=0)  # Nó do aluno
        for banda in bandas:
            G.add_node(banda, bipartite=1)  # Nó da banda
            G.add_edge(pessoa, banda)       # Aresta entre aluno e banda

# Identifica o conjunto de nós correspondentes a pessoas (bipartite=0)
pessoas = {n for n, d in G.nodes(data=True) if d['bipartite'] == 0}

# Gera posições automáticas para um layout bipartido
pos = bipartite_layout(G, pessoas)

# Calcula os graus dos nós para definir seus tamanhos no gráfico
graus = dict(G.degree())
tamanhos = [graus[n] * 300 for n in G.nodes()]  # Tamanho proporcional ao grau

# Configuração da visualização do grafo
plt.figure(figsize=(14, 10))
nx.draw(
    G, pos,
    with_labels=True,  # Exibe os nomes dos nós
    node_color=['skyblue' if n in pessoas else 'lightgreen' for n in G.nodes()],  # Cor por tipo de nó
    node_size=tamanhos,  # Tamanho proporcional ao número de conexões
    font_size=8,
    edge_color='gray'
)

# Título e exibição final
plt.title("Grafo de Incidência: Alunos de BCC e suas Bandas Favoritas")
plt.axis('off')  # Oculta os eixos
plt.show()
