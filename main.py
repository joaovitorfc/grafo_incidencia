import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import ast

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

G = nx.Graph()

for _, row in df.iterrows():
    pessoa = row['nome']
    bandas = row['bandas']
    
    
    G.add_node(pessoa, bipartite=0)
    
   
    for banda in bandas:
        G.add_node(banda, bipartite=1)
        G.add_edge(pessoa, banda)

from networkx.algorithms import bipartite

pessoas = {n for n, d in G.nodes(data=True) if d['bipartite']==0}
bandas = set(G) - pessoas

pos = dict()
pos.update((n, (1, i)) for i, n in enumerate(pessoas))
pos.update((n, (2, i)) for i, n in enumerate(bandas))

plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_color=['skyblue' if n in pessoas else 'lightgreen' for n in G.nodes()])
plt.title("Grafo de Incidência: Pessoas e suas Bandas Favoritas")
plt.show()