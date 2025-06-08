import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import ast
from collections import Counter
from networkx.drawing.layout import bipartite_layout 


data = {
    "nome": [
        "Luis Gustavo Dias Frigeri",
        "Marcos Vinicius",
        "Luiz Otávio Vieira Martins Guimarães",
        "Lucas Pereira",
        "Vitor",
        "João Celso da Silva Nogueira dos Santos",
        "Vinicius Oliveira",
        "Jonathan",
        "Portaluppi",
        "Rafael",
        "Luiz Felipe",
        "Karol",
        "Nicolas Augusto Cardoso",
        "Luiz Antônio Marcussi Neto",
        "Kaio Enrique",
        "Kendy H."
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

df = pd.DataFrame(data)
df['bandas'] = df['bandas'].apply(ast.literal_eval)

todas_bandas = [banda for lista in df['bandas'] for banda in lista]
contagem = Counter(todas_bandas)
bandas_populares = {banda for banda, freq in contagem.items() if freq >= 2}



G = nx.Graph()

for _, row in df.iterrows():
    pessoa = row['nome']
    bandas = set(row['bandas']).intersection(bandas_populares)
    if bandas:
        G.add_node(pessoa, bipartite=0)
        for banda in bandas:
            G.add_node(banda, bipartite=1)
            G.add_edge(pessoa, banda)

pessoas = {n for n, d in G.nodes(data=True) if d['bipartite'] == 0}
pos = bipartite_layout(G, pessoas)

graus = dict(G.degree())
tamanhos = [graus[n] * 300 for n in G.nodes()]

plt.figure(figsize=(14, 10))
nx.draw(
    G, pos,
    with_labels=True,
    node_color=['skyblue' if n in pessoas else 'lightgreen' for n in G.nodes()],
    node_size=tamanhos,
    font_size=8,
    edge_color='gray'
)
plt.title("Grafo de Incidência: Alunos de BCC e suas Bandas Favoritas")
plt.axis('off')
plt.show()